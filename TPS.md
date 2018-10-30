### TPS Competition Questionnaire

*Please replace the square brackets and the text in it with your answers*

**Number of CPUs**

24(Full Configuration) with limited access.

**Memory (GB)**

128G(Full Configuration) with limited access.

**Storage (GB)**

HDD 64G.

**Network**

10 Gbps Education LAN while the simulation only runs on one server cluster.

**Machine Type (Optional)**

Using a lab server cluster for baseband simulation for the next generation of communication.

**Command Lines for Running Cluster**
```
run.sh (See in Video)
# Test quarkchain
cd pyquarkchain/quarkchain/cluster
# 3 Clusters of miners
# Parameters set according to the competition guide
pypy3 multi_cluster.py --clean --num_clusters=3 --num_shards=64 --num_slaves=64 --root_block_interval_sec=180 --minor_block_interval_sec=30 --mine

monitor.sh (See in Video)
# Moniter quarkchain performance
cd pyquarkchain
quarkchain/tools/stats --ip=localhost

sim.sh (See in Video)
# Simulation of Transactions
pypy3 -c 'import jsonrpcclient; jsonrpcclient.request("http://localhost:38491", "createTransactions", numTxPerShard=120000, xShardPercent=5)'
```

**Peak TPS**

7253.40

**Video URL**

https://youtu.be/CEXjuJmKaWk

**Output From `stats` Tool**
(The result below is recorded during the screen video recording.)
```
----------------------------------------------------------------------------------------------------
                                      QuarkChain Cluster Stats                                      
----------------------------------------------------------------------------------------------------
CPU:                24
Memory:             128 GB
IP:                 localhost
Shards:             64
Servers:            64
Shard Interval:     30
Root Interval:      180
Syncing:            False
Mining:             True
Peers:              127.0.1.1:38293, 127.0.1.1:38292
----------------------------------------------------------------------------------------------------
Timestamp                     TPS   Pending tx  Confirmed tx       BPS      SBPS      ROOT       CPU
----------------------------------------------------------------------------------------------------
2018-10-30 20:28:31          0.00            0             0      0.22      0.00         1     75.00
2018-10-30 20:28:41          0.00            0             0      0.25      0.00         1      6.96
2018-10-30 20:28:52          0.00            0             0      0.37      0.00         1     12.06
2018-10-30 20:29:02          0.00            0             0      0.37      0.00         1     74.29
2018-10-30 20:29:12        741.33        39520         44480      0.50      0.00         1     35.41
2018-10-30 20:29:22       1112.00        29120         61150      0.57      0.00         1     29.16
2018-10-30 20:29:32       1270.35        31347         71208      0.63      0.00         1     28.43
2018-10-30 20:29:42       1688.10        86706         96273      0.63      0.00         1     26.43
2018-10-30 20:29:52       2188.20       158868        126279      0.60      0.00         1     28.45
2018-10-30 20:30:02       2802.50       208540        162550      0.58      0.00         1     49.19
2018-10-30 20:30:12       3901.52       221309        240229      0.70      0.00         1     53.34
2018-10-30 20:30:22       3694.05       211194        236628      0.78      0.00         1     54.87
2018-10-30 20:30:32       5025.17       427669        350438      0.83      0.00         1     53.00
2018-10-30 20:30:42       4815.45       357075        355158      0.97      0.00         1     39.33
2018-10-30 20:30:52       5444.67       429290        428080      0.98      0.00         1     36.55
2018-10-30 20:31:02       5724.33       431360        456010      1.03      0.00         1     44.81
2018-10-30 20:31:12       6691.67       525866        555841      1.10      0.00         2     32.85
2018-10-30 20:31:22       6848.97       559350        602074      1.13      0.00         2     40.27
2018-10-30 20:31:32       5751.60       493146        516510      1.17      0.00         2     26.72
2018-10-30 20:31:42       6288.33       568190        595650      1.15      0.00         2     34.11
2018-10-30 20:31:52       5774.17       653900        653940      1.07      0.00         2     53.01
2018-10-30 20:32:02       5312.25       603027        638829      1.08      0.00         2     41.02
2018-10-30 20:32:12       6493.85       744953        799271      1.08      0.00         2     32.87
2018-10-30 20:32:22       5475.43       862059        846989      0.92      0.00         2     36.61
2018-10-30 20:32:32       5400.82       885082        907962      0.90      0.00         2     33.22
2018-10-30 20:32:42       5290.50       799190        870120      0.97      0.00         2     24.62
2018-10-30 20:32:52       6379.63       818928       1031107      1.05      0.00         2     30.12
2018-10-30 20:33:02       5923.83       709580       1004450      1.07      0.00         2     27.12
2018-10-30 20:33:12       6330.17       647790       1067330      1.15      0.00         3     30.68
2018-10-30 20:33:22       7253.40       671891       1214741      1.20      0.00         3     18.95
2018-10-30 20:33:32       5923.65       510714       1033038      1.22      0.00         3     23.79
2018-10-30 20:33:42       6070.50       486828       1056924      1.25      0.00         3     14.33
2018-10-30 20:33:52       5306.25       462456       1081440      1.10      0.00         3     28.24
2018-10-30 20:34:02       5458.05       403164       1140732      1.15      0.00         4     30.59
2018-10-30 20:34:12       6153.95       457721       1429439      1.07      0.00         4     27.73
2018-10-30 20:34:22       5485.50       346470       1369290      1.08      0.00         4     21.07
2018-10-30 20:34:32       5398.00       313260       1402500      1.07      0.00         4     16.19
2018-10-30 20:34:42       4959.15       236988       1307340      1.10      0.00         4     22.22
2018-10-30 20:34:52       5523.33       240910       1475010      1.12      0.00         4     13.27
2018-10-30 20:35:02       5064.15       201861       1342611      1.13      0.00         4     18.75
2018-10-30 20:35:12       5572.50       164110       1552290      1.15      0.00         4     25.01
2018-10-30 20:35:22       5266.17       128680       1588040      1.12      0.00         5     19.60
2018-10-30 20:35:32       5031.58        97350       1791218      1.07      0.00         5     23.60
```

**Additional Comment**

Due to the precious computation resources of our labs server cluster, I only have half an hour of access, so the time recorded above may not satisfy the requirement of 10 minutes.
However, I tried my best to record for 8 minutes long simulation and got a not so bad result. Greately appreciate for your understanding!
