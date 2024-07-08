import json

from utils.tools import get_accounts_data

with open('abi/swaprouter.json', 'r') as file:
    QUICKSWAP_ROUTER_ABI = json.load(file)

with open('abi/activity_log.json', 'r') as file:
    ACTIVITY_LOG_ABI = json.load(file)

result = get_accounts_data()
if result is None:
    print("Failed to get accounts data. Please check your Excel file and settings.")
else:
    ACCOUNT_NAMES, PRIVATE_KEYS, PROXIES, USER_AGENT = result
