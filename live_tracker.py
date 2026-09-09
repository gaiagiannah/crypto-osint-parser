
import time
from web3 import Web3

def connect_to_live_ethereum():
    # SWAP THIS LINE: Replace the overloaded Cloudflare URL with a highly stable alternative
    rpc_url = "https://ankr.com"  # Alternative backup: "https://llamarpc.com"
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    print("[*] Initializing network handshake with Ethereum Mainnet node...")
    # ... (keep the rest of the script exactly the same)
    
    if w3.is_connected():
        print(f"[+] Connection Established Successfully!")
        # Fetching basic global chain metadata
        current_block = w3.eth.block_number
        gas_price_gwei = w3.from_wei(w3.eth.gas_price, 'gwei')
        
        print(f"    Current Global Block Height: #{current_block}")
        print(f"    Live Network Gas Price:      {gas_price_gwei:.2f} Gwei")
        return w3
    else:
        print("[-] Critical Connection Failure: Web3 endpoint unreachable.")
        return None

def scan_latest_live_block(w3_instance):
    """
    Pulls the absolute latest block processed on the blockchain network
    and iterates through every single live transaction to locate mixing indicators.
    """
    print("\n" + "="*60)
    print("🌪️ LIVE TRACKER ENGINE: DISPATCHING BLOCK RECONNAISSANCE")
    print("="*60)
    
    # Documented high-volume Tornado Cash pool contracts to watch for flags
    MIXER_SIGNATURES = {
        "0x12D66f87A04A9E220743712ce6d9bBb1b5616B8fc".lower(): "Tornado.Cash 0.1 ETH Pool",
        "0x47CE0C6eD5b0Eb3933091c92A07ff1c0Cf742961".lower(): "Tornado.Cash 1 ETH Pool",
        "0x910CBD523D972EB0A6F4cae0ECE369aB7a664df7".lower(): "Tornado.Cash 10 ETH Pool",
        "0xA160cdAB4576E2C124c1883CFb75117A3A2a2d30".lower(): "Tornado.Cash 100 ETH Pool"
    }

    try:
        # Get the latest block details, including full transaction objects
        latest_block = w3_instance.eth.get_block('latest', full_transactions=True)
        block_num = latest_block['number']
        transactions = latest_block['transactions']
        
        print(f"[*] Intercepted Block #{block_num}. Parsing {len(transactions)} live network transactions...")
        time.sleep(1)
        
        flag_count = 0
        
        # Scan through every live payment happening on Earth right now in this block
        for tx in transactions:
            # Safely extract the recipient address (can be None if it's a contract deployment)
            recipient = tx.get('to')
            
            if recipient:
                recipient_lowercase = recipient.lower()
                
                # Check if someone is trying to route money into a privacy mixer right now
                if recipient_lowercase in MIXER_SIGNATURES:
                    tx_hash = tx['hash'].hex()
                    value_eth = w3_instance.from_wei(tx['value'], 'ether')
                    sender = tx['from']
                    
                    print(f"\n🚨 [MIXER INTERCEPT] Active transaction flagged in block #{block_num}!")
                    print(f"    Transaction Hash: {tx_hash}")
                    print(f"    Origin Originator: {sender}")
                    print(f"    Mixer Destination: {MIXER_SIGNATURES[recipient_lowercase]}")
                    print(f"    Value Deposited:  {value_eth} ETH")
                    flag_count += 1
        
        if flag_count == 0:
            print(f"[+] Scan Complete for Block #{block_num}. Result: Clean. No public mixer logs triggered.")
            
    except Exception as e:
        print(f"[-] Execution Interrupted during live block extraction: {e}")

if __name__ == "__main__":
    # Boot the live tracker
    web3_connection = connect_to_live_ethereum()
    
    if web3_connection:
        # Run a scan on the latest block configuration data
        scan_latest_live_block(web3_connection)