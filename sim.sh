# Simulation of Transactions
pypy3 -c 'import jsonrpcclient; jsonrpcclient.request("http://localhost:38491", "createTransactions", numTxPerShard=120000, xShardPercent=5)'
