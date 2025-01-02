import random
import time
from web3 import Web3
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# User Configurations
PRIVATE_KEY = os.getenv('PRIVATE_KEY')  # Add your private key to .env
MIN_AMOUNT = float(input("Enter minimum transfer amount: ").strip())
MAX_AMOUNT = float(input("Enter maximum transfer amount: ").strip())
LOOP_COUNT = int(input("Enter the number of transactions to loop: ").strip())

# Load recipient addresses
with open("address.txt", "r") as file:
    recipient_addresses = [line.strip() for line in file if line.strip()]

if not recipient_addresses:
    raise ValueError("No recipient addresses found in address.txt.")

# Haust Testnet Configuration
RPC_URL = "https://rpc-test.haust.network"
CHAIN_ID = 1570754601
CURRENCY_SYMBOL = "HAUST"

# Connect to Blockchain
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Verify Connection
if web3.is_connected():
    print(f"✅ Connected to Haust Testnet ({RPC_URL})")
else:
    raise ConnectionError("❌ Failed to connect to Haust Testnet!")

# Derive sender address from private key
SENDER_ADDRESS = web3.eth.account.from_key(PRIVATE_KEY).address
print(f"🔑 Wallet Address: {SENDER_ADDRESS}")

# Function to send a transaction
def send_transaction(sender, recipient, amount, private_key):
    try:
        nonce = web3.eth.get_transaction_count(sender)
        gas_price = web3.eth.gas_price

        tx = {
            'nonce': nonce,
            'to': recipient,
            'value': web3.to_wei(amount, 'ether'),
            'gas': 21000,
            'gasPrice': gas_price,
            'chainId': CHAIN_ID,
        }

        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
        
        print(f"✅ Transaction sent! Tx Hash: {tx_hash.hex()}")
        print(f"🔗 Explorer: https://explorer-test.haust.network/tx/{tx_hash.hex()}")
        return tx_hash.hex()

    except Exception as e:
        print(f"❌ Transaction failed: {e}")
        return None

# Main Loop for Transactions
def main():
    recipient_index = 0
    num_recipients = len(recipient_addresses)  # Total number of recipients
    for i in range(LOOP_COUNT):
        amount = random.uniform(MIN_AMOUNT, MAX_AMOUNT)
        recipient = recipient_addresses[recipient_index]
        print(f"\n🔄 Loop {i + 1}/{LOOP_COUNT}")
        print(f"💸 Sending {amount:.6f} {CURRENCY_SYMBOL} to {recipient}")
        
        tx_hash = send_transaction(SENDER_ADDRESS, recipient, amount, PRIVATE_KEY)
        
        if tx_hash:
            print(f"✅ Transaction Successful: {tx_hash}")
        else:
            print("❌ Transaction Failed, stopping further execution.")
            break

        # Move to the next recipient address
        recipient_index = (recipient_index + 1) % num_recipients

        # Delay with random sleep time between 12 and 25 seconds
        sleep_time = random.randint(12, 25)
        print(f"⏳ Waiting for {sleep_time} seconds before the next transaction...")
        time.sleep(sleep_time)

# Entry Point
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Script terminated by user.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
