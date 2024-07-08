networks = {
    "bscMainnet": {
        "name": "bscMainnet",
        "rpc": "https://bsc-dataseed.bnbchain.org",
        "chain_id": 56,
        "eip1559_support": True,
        "token": "BNB",
        "explorer": "https://bscscan.com/",
        "decimals": 18
    },
    "bscTestnet": {
        "name": "bscTestnet",
        "rpc": "https://data-seed-prebsc-1-s1.bnbchain.org:8545",
        "chain_id": 97,
        "eip1559_support": True,
        "token": "BNB",
        "explorer": "https://testnet.bscscan.com/",
        "decimals": 18
    },
    "xLayerTestnet": {
        "name": "xLayerTestnet",
        "rpc": "https://testrpc.x1.tech",
        "chain_id": 195,
        "eip1559_support": False,
        "token": "OKB",
        "explorer": "https://www.okx.com/web3/explorer/xlayer-test/",
        "decimals": 18
    }
}


def get_network_by_name(name):
    return networks.get(name, None)
