import json

from web3 import Web3

appium_server_url = 'http://127.0.0.1'
base_appium_port = 4723
key1 = 'Vey3L99fbmhGTEW'
username = 'abhi-worldz#0077'
# Reference screen size (the size for which your original coordinates were defined)
REFERENCE_WIDTH = 1080
REFERENCE_HEIGHT = 2340

with open('abi/swaprouter.json', 'r') as file:
    QUICKSWAP_ROUTER_ABI = json.load(file)

with open('abi/activity_log.json', 'r') as file:
    ACTIVITY_LOG_ABI = json.load(file)

with open('abi/nft.json', 'r') as file:
    NFT_CONTRACT_ABI = json.load(file)

with open('abi/marketplace.json', 'r') as file:
    MARKETPLACE_ABI = json.load(file)

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"

ETH_MASK = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"

TOKENS_PER_CHAIN = {
    'bscTestnet': {
        "WBNB": "",
        "WBTC": "",
        "WETH": "",
    },
    'bscMainnet': {
        "WBNB": "",
        "WBTC": "",
        "WETH": "",
    },
    'xLayerTestnet': {
        "WBNB": Web3.to_checksum_address("0x87a851c652e5d772ba61ec320753c6349bb3c1e3"),
        "WETH": Web3.to_checksum_address("0xbec7859bc3d0603bec454f7194173e36bf2aa5c8"),
        "USDC": Web3.to_checksum_address("0xcd65196488b2e2fbcbc3e5d675b3108f4935e64a"),
        "USDT": ""
    },
}

PANCAKE_CONTRACTS = {
    "bscTestnet": {
        "router": "",
    },
    "bscMainnet": {
        "router": "",
    },
    "xLayerTestnetRPC": {
        "router": "",
    },
}
MARKETPLACE_CONTRACTS = {"xLayerTestnet": "0xaD2790eB4e47A78fe908B79C1eF35e528f840661"}
NFT_CONTRACTS = {"xLayerTestnet": "0xbCf775eF3455E433D68D12c21b0394d8992C18c5"}
QUICKSWAP_CONTRACTS = {"xLayerTestnet": "0x6c28AeF8977c9B773996d0e8376d2EE379446F2f"}
ACTIVITY_CONTRACTS = {
    "xLayerTestnet": {
        "pvp": "0xd2EDDbDAefEA8312402A0B5C4A59075Ea57B2C87",
        "battle": "0xf8295397a2523b425473aE3aFc35E525D13A962d",
        "activity": "0x7aC335aE919BFC861faE0a64AAE9E0fE6AC5A345"
    },
    "xLayerMainnet": {
        "pvp": "",
        "battle": "",
        "activity": ""
    },
}

HELP_SOFTWARE = True  # True or False | True = You support me 1% amount of transactions on aggregator`s

CHAIN_NAME = {97: "bscTestNet", 56: "bscMainNet", 195: "xLayerTestnet"}

IMAP_CONFIG = {
    "outlook.com": "outlook.office365.com",
    "hotmail.com": "imap-mail.outlook.com",
}

NUM_THREADS = 3
PROVIDER_URL = "https://data-seed-prebsc-1-s1.bnbchain.org:8545"
EXPLORER_URL = "https://testnet.bscscan.com/"
MAX_AMOUNT_ROTATION = 0.01

ENV = "xLayerTestnet"


def update_environment():
    ENV = "xLayerMainnet"


JSON_FILE_PATH = "../addresses.json"

GOOGLE_SHEETS_LINK = "'https://docs.google.com/spreadsheets/d/1FBykrPhwggansxMedmB3SPwFdra0g3OuinXjfKK24QE'"

TITLE = """
CreoPlay
"""
"""------------------------------------------------GENERAL SETTINGS--------------------------------------------------------
    WALLETS_TO_WORK = 0 | The software will take wallets from the table according to the rules described below
    0       = all wallets in sequence
    3       = only wallet No. 3
    4, 20   = wallets No. 4 and No. 20
    [5, 25] = wallets from No. 5 to No. 25

    ACCOUNTS_IN_STREAM      | Number of wallets in the stream to execute. If there are 100 wallets in total, and 10 is specified,
                                then the software will make 10 rounds of 10 wallets each

    EXCEL_PASSWORD          | Enables password prompt when entering the software. First, set the password in the table
    EXCEL_PAGE_NAME         | The name of the sheet in the table. Example: 'creoPlay'

"""

SOFTWARE_MODE = 1  # 0 - sequential start / 1 - parallel start
ACCOUNTS_IN_STREAM = 10  # Number of accounts in the stream when SOFTWARE_MODE = 1
WALLETS_TO_WORK = 0  # 0 / 3 / 3, 20 / [3, 20]
BREAK_ROUTE = False  # Stops the route execution if an error occurs
SHUFFLE_WALLETS = True  # Shuffles wallets before starting
SAVE_PROGRESS = False  # Enables saving of account progress for Classic-routes
TELEGRAM_NOTIFICATIONS = False  # Enables notifications in Telegram

"------------------------------------------------SLEEP CONTROL---------------------------------------------------------"
SLEEP_MODE = False  # Enables sleep after each module and account
SLEEP_TIME_MODULES = (30, 60)  # (minimum, maximum) seconds | Sleep time between modules.
SLEEP_TIME_ACCOUNTS = (
    60,
    120,
)  # (minimum, maximum) seconds | Sleep time between accounts.

"------------------------------------------------RETRY CONTROL---------------------------------------------------------"
MAXIMUM_RETRY = 20  # Number of retries in case of errors
SLEEP_TIME_RETRY = (
    5,
    10,
)  # (minimum, maximum) seconds | Sleep time after each retry

"------------------------------------------------PROXY CONTROL---------------------------------------------------------"
MOBILE_PROXY = False  # Enables the use of mobile proxies.
MOBILE_PROXY_URL_CHANGER = [
    "",
    "",
    "",
]  # ['link1', 'link2'..] | Links for changing IP. The software will go through all the links, you can specify several proxies in Excel

"------------------------------------------------SECURE DATA-----------------------------------------------------------"
# https://2captcha.com/enterpage
TWO_CAPTCHA_API_KEY = "b5cac476a42c69cd0e150fab88332a51"

# EXCEL AND GOOGLE INFO
EXCEL_PASSWORD = False
EXCEL_PAGE_NAME = "Sheet"
EXCEL_FILE_PATH = "./data/registration_data.xlsx"  # You can leave it unchanged if you are satisfied with the default table location
JSON_FILE_PATH = "./addresses.json"

# TELEGRAM DATA
TG_TOKEN = ""  # https://t.me/BotFather
TG_ID = ""  # https://t.me/getmyid_bot

"""
--------------------------------------------CLASSIC-ROUTES CONTROL------------------------------------------------------

    mint_creoPlay_tokens           # mint $BNB on creoPlay Faucet (https://artio.faucet.creoPlay.com/)
    transfer_bnb                   # swap on BEX ($BNB -> $BTC)
    swap_eth_bex                    # swap on BEX ($BNB -> $ETH)
          
    Select the necessary modules for interaction
    You can create any route, the software will work strictly according to it. For each list, one module will be selected
    into the route, if the software selects None, it will skip that list of modules.
    The list of modules is above.

    CLASSIC_ROUTES_MODULES_USING = [
        ['transfer_bnb'],
        ['mint_nft'],
        ['make_market_item'],
        ['create_market_sale'],
        ['swap_quickswap_okx_usdc'],
        ['buy_creo_token'],
        ['save_pvp_log'],
        ['save_battle_log'],
        ['save_activity_log'],
        ['transfer_okb']
        ...
    ]
"""
CLASSIC_ROUTES_MODULES_USING = [
    'transfer_okb',
    'swap_quickswap_okx_usdc',
    'mint_nft',
    'create_market_sale',
    'make_market_item'
]
