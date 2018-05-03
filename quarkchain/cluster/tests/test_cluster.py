import asyncio
import unittest

from quarkchain.cluster.tests.test_utils import create_transfer_transaction, get_test_env
from quarkchain.cluster.utils import create_cluster_config
from quarkchain.cluster.slave import SlaveServer
from quarkchain.cluster.master import MasterServer, ClusterConfig
from quarkchain.cluster.root_state import RootState
from quarkchain.core import Address, Identity, ShardMask


def create_test_clusters(numCluster, genesisAccount=Address.createEmptyAccount()):
    portStart = 38000
    seedPort = portStart
    clusterList = []
    loop = asyncio.get_event_loop()

    for i in range(numCluster):
        env = get_test_env(genesisAccount, genesisMinorQuarkash=1000000)

        p2pPort = portStart
        config = create_cluster_config(
            slaveCount=env.config.SHARD_SIZE,
            ip="127.0.0.1",
            p2pPort=p2pPort,
            clusterPortStart=portStart + 1,
        )
        portStart += (1 + env.config.SHARD_SIZE)

        env.config.P2P_SERVER_PORT = p2pPort
        env.config.P2P_SEED_PORT = seedPort
        env.clusterConfig.ID = 0
        env.clusterConfig.CONFIG = ClusterConfig(config)

        slaveServerList = []
        for slave in range(env.config.SHARD_SIZE):
            slaveEnv = env.copy()
            slaveEnv.clusterConfig.ID = config["slaves"][slave]["id"]
            slaveEnv.clusterConfig.NODE_PORT = config["slaves"][slave]["port"]
            slaveEnv.clusterConfig.SHARD_MASK_LIST = [ShardMask(v) for v in config["slaves"][slave]["shard_masks"]]
            slaveServer = SlaveServer(slaveEnv)
            slaveServer.start()
            slaveServerList.append(slaveServer)

        masterServer = MasterServer(env, RootState(env, createGenesis=True))
        masterServer.start()

        # Wait until the cluster is ready
        loop.run_until_complete(masterServer.clusterActiveFuture)

        clusterList.append((masterServer, slaveServerList))

    return clusterList


def shutdown_clusters(clusterList):
    loop = asyncio.get_event_loop()

    for cluster in clusterList:
        master, slaveList = cluster

        for slave in slaveList:
            slave.shutdown()
            loop.run_until_complete(slave.getShutdownFuture())

        master.shutdown()
        loop.run_until_complete(master.getShutdownFuture())


def sync_run(coro):
    return asyncio.get_event_loop().run_until_complete(coro)


class TestCluster(unittest.TestCase):

    def testSingleCluster(self):
        id1 = Identity.createRandomIdentity()
        acc1 = Address.createFromIdentity(id1, fullShardId=0)
        clusters = create_test_clusters(1, acc1)
        shutdown_clusters(clusters)

    def testThreeClusters(self):
        clusters = create_test_clusters(3)
        shutdown_clusters(clusters)

    def testGetNextBlockToMine(self):
        id1 = Identity.createRandomIdentity()
        acc1 = Address.createFromIdentity(id1, fullShardId=0)
        acc2 = Address.createRandomAccount(fullShardId=0)
        acc3 = Address.createRandomAccount(fullShardId=1)

        clusters = create_test_clusters(1, acc1)
        master, slaves = clusters[0]

        tx = create_transfer_transaction(
            shardState=slaves[0].shardStateMap[2 | 0],
            fromId=id1,
            toAddress=acc2,
            amount=12345,
        )
        self.assertTrue(slaves[0].addTx(tx))

        # Expect to mine shard 0 since it has one tx
        isRoot, block1 = sync_run(master.getNextBlockToMine(address=acc1))
        self.assertFalse(isRoot)
        self.assertEqual(block1.header.height, 1)
        self.assertEqual(block1.header.branch.value, 2 | 0)
        self.assertEqual(len(block1.txList), 1)

        self.assertTrue(sync_run(slaves[0].addBlock(block1)))

        # Expect to mine shard 1 due to proof-of-progress
        isRoot, block2 = sync_run(master.getNextBlockToMine(address=acc3))
        self.assertFalse(isRoot)
        self.assertEqual(block2.header.height, 1)
        self.assertEqual(block2.header.branch.value, 2 | 1)
        self.assertEqual(len(block2.txList), 0)

        self.assertTrue(sync_run(slaves[1].addBlock(block2)))

        # Expect to mine root
        isRoot, block = sync_run(master.getNextBlockToMine(address=Address.createEmptyAccount()))
        self.assertTrue(isRoot)
        self.assertEqual(block.header.height, 1)
        self.assertEqual(len(block.minorBlockHeaderList), 2)
        self.assertEqual(block.minorBlockHeaderList[0], block1.header)
        self.assertEqual(block.minorBlockHeaderList[1], block2.header)

        self.assertTrue(master.rootState.addBlock(block))
        shutdown_clusters(clusters)
