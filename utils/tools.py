import io
import json
import random
import time
from getpass import getpass

import msoffcrypto
import pandas as pd
from eth_account import Account
from termcolor import cprint
from web3 import Web3
from web3.exceptions import TransactionNotFound

from utils.constants import EXCEL_PASSWORD, EXCEL_PAGE_NAME, EXCEL_FILE_PATH, ENV
from .networks import get_network_by_name

network = get_network_by_name(ENV)
provider_url = network['rpc']
web3 = Web3(Web3.HTTPProvider(provider_url))


def clean_progress_file():
    with open("./data/services/wallets_progress.json", "w") as file:
        file.truncate(0)


def get_accounts_data():
    try:
        file = open(EXCEL_FILE_PATH, "rb")
        if EXCEL_PASSWORD:
            decrypted_data = io.BytesIO()
            office_file = msoffcrypto.OfficeFile(file)
            password = getpass("⚔️ Enter the password degen: ")
            try:
                office_file.load_key(password=password)
                office_file.decrypt(decrypted_data)
                wb = pd.read_excel(decrypted_data, sheet_name=EXCEL_PAGE_NAME)
            except (msoffcrypto.exceptions.DecryptionError, msoffcrypto.exceptions.InvalidKeyError):
                cprint("\n⚠️ Incorrect password or Excel file issue! ⚠️", color="light_red", attrs=["blink"])
                return None
        else:
            wb = pd.read_excel(file, sheet_name=EXCEL_PAGE_NAME)

        accounts_data = {}
        for index, row in wb.iterrows():
            accounts_data[int(index) + 1] = {
                "account_number": row.get("username"),
                "private_key": row.get("privateKey"),
                "proxy": row.get("proxy_url"),
                "user_agent": row.get("user_agent"),
            }

        acc_names = [str(v["account_number"]) for v in accounts_data.values() if v["account_number"]]
        private_keys = [v["private_key"] for v in accounts_data.values() if v["private_key"]]
        proxies = [v["proxy"] for v in accounts_data.values() if v["proxy"]]
        user_agents = [v["user_agent"] for v in accounts_data.values() if v["user_agent"]]
        public_keys = [web3.eth.account.from_key(pk).address for pk in private_keys]

        with open("addresses.json", "w") as json_file:
            json.dump({"addresses": public_keys}, json_file, indent=4)

        return acc_names, private_keys, proxies, user_agents

    except ValueError as error:
        cprint(f"\n⚠️ Excel reading error: {error} ⚠️", color="light_red", attrs=["blink"])
    except FileNotFoundError:
        cprint(f"\n⚠️ Excel file not found: {EXCEL_FILE_PATH} ⚠️", color="light_red", attrs=["blink"])
    except Exception as error:
        cprint(f"\n⚠️ Unexpected error: {error} ⚠️", color="light_red", attrs=["blink"])

    return None


def get_random_wallet():
    accounts_data = get_accounts_data()
    if accounts_data is None:
        print("Failed to get account data.")
        return None

    _, private_keys, _, _ = accounts_data
    if not private_keys:
        print("No private keys found.")
        return None

    random_private_key = random.choice(private_keys)
    random_public_key = Account.from_key(random_private_key).address
    return random_private_key, random_public_key,


def get_all_wallets():
    accounts_data = get_accounts_data()
    if accounts_data is None:
        print("Failed to get account data.")
        return None

    _, private_keys, _, _ = accounts_data
    if not private_keys:
        print("No private keys found.")
        return None

    public_keys = [web3.eth.account.from_key(pk).address for pk in private_keys]
    return public_keys


def get_priority_fee():
    fee_history = web3.eth.fee_history(25, "latest", [20.0])
    non_empty_block_priority_fees = [
        fee[0] for fee in fee_history["reward"] if fee[0] != 0
    ]
    divisor_priority = max(len(non_empty_block_priority_fees), 1)
    priority_fee = int(round(sum(non_empty_block_priority_fees) / divisor_priority))
    return priority_fee


def prepare_transaction(address, value: int = 0):
    try:
        network = get_network_by_name(ENV)
        tx_params = {
            "from": web3.to_checksum_address(address),
            "nonce": web3.eth.get_transaction_count(address),
            "value": value,
            "chainId": network["chain_id"],
        }

        if network["eip1559_support"]:
            base_fee = web3.eth.gas_price
            max_priority_fee_per_gas = get_priority_fee()
            max_fee_per_gas = base_fee + max_priority_fee_per_gas

            tx_params["maxPriorityFeePerGas"] = max_priority_fee_per_gas
            tx_params["maxFeePerGas"] = int(max_fee_per_gas * 1.5)
            tx_params["type"] = "0x2"
        else:
            tx_params["gasPrice"] = int(web3.eth.gas_price * 1.5)

        return tx_params
    except Exception as error:
        print(f"{(error)}")


def send_transaction(
        transaction,
        private_key,
        without_gas=False,
        poll_latency=10,
        timeout=360,
):
    try:
        network = get_network_by_name(ENV)
        explorer = network['explorer']
        network_name = network["name"]
        if not without_gas:
            transaction["gas"] = int((web3.eth.estimate_gas(transaction)) * 1.5)

        signed_tx = web3.eth.account.sign_transaction(transaction, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Transaction sent: {explorer}tx/{tx_hash.hex()}")
        total_time = 0
        timeout = timeout if network_name != "Polygon" else 1200
        start_time = time.time()
        while True:
            try:
                receipts = web3.eth.get_transaction_receipt(tx_hash)
                status = receipts.get("status")
                if status == 1:
                    print(f"Transaction sent: {explorer}tx/{tx_hash.hex()}")
                    return f"{explorer}tx/{tx_hash.hex()}"
                elif status == 0:
                    time.sleep(poll_latency)
                else:

                    return f"{explorer}tx/{tx_hash.hex()}"
            except TransactionNotFound:
                if time.time() - start_time >= timeout:
                    return f"{explorer}tx/{tx_hash.hex()}"
                time.sleep(poll_latency)
    except Exception as error:
        print(str(error))
