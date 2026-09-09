
import time

# =====================================================================
# CONCEPT 1: CLUSTERING LOGIC (The Co-Spend Heuristic)
# =====================================================================
def simulate_wallet_clustering(transaction_inputs):
    """
    Core Rule: If Wallet A and Wallet B are used together as inputs to pay 
    for a single transaction, they MUST be controlled by the same private key holder.
    This allows investigators to group hundreds of anonymous wallets into one 'Entity'.
    """
    print("\n" + "="*60)
    print("🔬 FORENSICS MODULE 1: WALLET CLUSTERING (CO-SPEND HEURISTIC)")
    print("="*60)
    print(f"[*] Analyzing blockchain transaction inputs: {transaction_inputs}")
    time.sleep(1)
    
    # Clustering engine algorithm
    suspected_entity_cluster = set(transaction_inputs)
    
    print(f"[+] HEURISTIC TRIGGERED: Multiple inputs detected in a single Tx block.")
    print(f"[-] Result: Wallets {list(suspected_entity_cluster)} have been CLUSTERED.")
    print(f"🎯 Action: These wallets now share a single identity tag: [Target_Hacker_Group_01]")
    return suspected_entity_cluster


# =====================================================================
# CONCEPT 2: UNRAVELING OBFUSCATION (Peeling Chains & Cross-Chain Hops)
# =====================================================================
def trace_peeling_chain(initial_stolen_amount, initial_wallet):
    """
    Criminals rarely move $10 Million at once. They use a 'Peeling Chain'.
    They send a tiny bit to an exchange to cash out, and peel the remaining 
    change to a brand new wallet. They repeat this hundreds of times.
    """
    print("\n" + "="*60)
    print("⛓️ FORENSICS MODULE 2: UNRAVELING A PEELING CHAIN")
    print("="*60)
    print(f"[*] Starting trace at Root Wallet: {initial_wallet} (Amount: {initial_stolen_amount} ETH)")
    time.sleep(1)
    
    current_wallet = initial_wallet
    current_balance = initial_stolen_amount
    peel_count = 1
    
    # Simulating tracing the chain automatically
    while current_balance > 5:
        peel_amount = 2.5  # Stolen cash sent to an exchange exit ramp
        change_remaining = current_balance - peel_amount - 0.01 # Bypassing gas fees
        
        # Simulating a new change address being generated dynamically
        next_wallet = f"0xChangeWallet_Hop_{peel_count}..." 
        
        print(f"\n[Peel #{peel_count}] Followed transaction flow:")
        print(f"   From: {current_wallet}")
        print(f"   ↳ Sent to Cash-out Point:  {peel_amount} ETH")
        print(f"   ↳ Peeled to Next Address: {change_remaining:.2f} ETH -> {next_wallet}")
        
        # Investigator logic overrides the hop
        current_wallet = next_wallet
        current_balance = change_remaining
        peel_count += 1
        time.sleep(0.8)
        
    print(f"\n[+] PEELING CHAIN UNRAVELED: Traced funds successfully through {peel_count-1} layers of obfuscation.")


# =====================================================================
# CONCEPT 3: MIXER DETECTOR CODES
# =====================================================================
def scan_for_privacy_mixers(wallet_transaction_history):
    """
    Mixers use fixed smart contract pools to break the link between sender and receiver.
    We can program our engine to check if a wallet interacts with known mixer contracts.
    """
    print("\n" + "="*60)
    print("🌪️ FORENSICS MODULE 3: PRIVACY MIXER DETECTION INTERCEPT")
    print("="*60)
    
    # Database of known illicit contract addresses (e.g., Tornado Cash smart contracts)
    KNOWN_MIXER_CONTRACTS = {
        "0x12d66f87a04a9e220743712ce6d9bb1b5616b8fc": "Tornado.Cash: 0.1 ETH Pool",
        "0x47ce0c6ed5b0eb3933091c92a07ff1c0cf742961": "Tornado.Cash: 1 ETH Pool",
        "0x910cbd523d972eb0a6f4cae0ece369ab7a664df7": "Tornado.Cash: 10 ETH Pool",
        "0xa160cdab4576e2c124c1883cfb75117a3a2a2d30": "Tornado.Cash: 100 ETH Pool"
    }
    
    for tx in wallet_transaction_history:
        destination_address = tx["to"].lower()
        amount_sent = tx["value"]
        
        print(f"[*] Scanning Tx: {tx['tx_hash'][:15]}... Sent {amount_sent} ETH to {destination_address[:20]}...")
        time.sleep(0.5)
        
        if destination_address in KNOWN_MIXER_CONTRACTS:
            print(f"     CRITICAL FLAG: Privacy Obfuscation Attempt Intercepted!")
            print(f"     Destination matches known smart contract: {KNOWN_MIXER_CONTRACTS[destination_address]}")
            print(f"     RISK ASSESSMENT SCORE: 100/100 (HIGH RISK)")
            return True
            
    print("[+] Scan Clean: No known crypto mixer links detected in immediate transactions.")
    return False


if __name__ == "__main__":
    # RUNNING THE SIMULATED INVESTIGATION
    
    # 1. Test Clustering Logic
    # Scenario: A hacker uses three different wallets to fund one single attack payload
    active_inputs = ["0xHackerWallet_A", "0xHackerWallet_B", "0xHackerWallet_C"]
    cluster_results = simulate_wallet_clustering(active_inputs)
    
    # 2. Test Peeling Chain Unraveling
    # Scenario: Tracer follows 10 ETH being split up repeatedly down a chain
    trace_peeling_chain(initial_stolen_amount=10.0, initial_wallet="0xRoot_Hacker_Vault")
    
    # 3. Test Privacy Mixer Detector
    # Scenario: Simulated raw blockchain transactions pulled via an API
    simulated_api_transactions = [
        {"tx_hash": "0xabc123abc123abc123", "to": "0xMerchantStoreAddress123", "value": 0.5},
        {"tx_hash": "0xdef456def456def456", "to": "0x910cbd523d972eb0a6f4cae0ece369ab7a664df7", "value": 10.0}, # Points to 10 ETH Mixer
        {"tx_hash": "0xghi789ghi789ghi789", "to": "0xFriendWalletAddress456", "value": 1.2}
    ]
    scan_for_privacy_mixers(simulated_api_transactions)