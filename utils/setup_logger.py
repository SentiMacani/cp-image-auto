import logging
import csv
from datetime import datetime
import os

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('genleap_verbose')
logger.setLevel(logging.DEBUG)

def write_transaction_to_csv(username, activity_type, tx_hash, status, description):
    csv_file = 'transactions.csv'
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Timestamp', 'Username', 'Activity Type', 'Transaction Hash', 'Status', 'Description'])
        
        writer.writerow([
            datetime.now().isoformat(),
            username,
            activity_type,
            tx_hash,
            status,
            description
        ])

# Add this function to the logger
def log_transaction(username, activity_type, tx_hash, status, description):
    write_transaction_to_csv(username, activity_type, tx_hash, status, description)
    logger.info(f"Transaction logged: {username}, {activity_type}, {tx_hash}, {status}")

# Monkey-patch the logger to include the new method
logger.log_transaction = log_transaction