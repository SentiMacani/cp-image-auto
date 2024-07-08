import json
import os
from dotenv import load_dotenv
from web3 import Web3
from utils.setup_logger import logger


load_dotenv()

private_key = str(os.getenv("PRIVATE_KEY"))
with open('abi/activity_log.json', 'r') as file:
    ACTIVITY_LOG_ABI = json.load(file)

web3 = Web3(Web3.HTTPProvider('https://testrpc.x1.tech'))
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

# TO DO: add max retry logic when gas error occurs
def save_activity_log(self, username, description, activity_type):
    try:
        contract = web3.eth.contract(address=ACTIVITY_CONTRACTS["xLayerTestnet"][activity_type], abi=ACTIVITY_LOG_ABI)
        account = web3.eth.account.from_key(private_key)
        address = account.address
        current_gas_price = web3.eth.gas_price

        estimated_gas = contract.functions.saveActivity(username, description).estimate_gas({
            'from': address,
        })

        txn = contract.functions.saveActivity(username, description).build_transaction({
            'chainId': 195,
            'gas': estimated_gas + 1000,
            'gasPrice': current_gas_price,
            'nonce': web3.eth.get_transaction_count(address),
        })

        signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        tx_hash_hex = web3.to_hex(tx_hash)
        
        # Log the successful transaction
        logger.log_transaction(username, activity_type, tx_hash_hex, 'Success', description)
        
        return tx_hash_hex
    except Exception as e:
        error_message = str(e)
        # Log the failed transaction
        logger.log_transaction(username, activity_type, 'N/A', 'Failed', f"Error: {error_message}")
        print(f"transaction failed {error_message}")
        return None