# Test quarkchain
cd pyquarkchain/quarkchain/cluster
# 3 Clusters of miners
# Parameters set according to the competition guide
pypy3 multi_cluster.py --clean --num_clusters=3 --num_shards=64 --num_slaves=64 --root_block_interval_sec=180 --minor_block_interval_sec=30 --mine
