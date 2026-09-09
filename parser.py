

import re

def extract_crypto_wallets(scraped_text):
    # REGEX PATTERNS
    btc_pattern = r'\b(?:1|3)[a-km-zA-HJ-NP-Z1-9]{26,33}\b|\bbc1[a-zA-HJ-NP-Z0-9]{39,59}\b'
    eth_pattern = r'\b0x[a-fA-F0-9]{40}\b'
    sol_pattern = r'\b[1-9A-HJ-NP-Za-km-z]{32,44}\b'
    
    print("[*] Processing raw text dump for crypto signatures...")
    
    found_btc = re.findall(btc_pattern, scraped_text)
    found_eth = re.findall(eth_pattern, scraped_text)
    found_sol_raw = re.findall(sol_pattern, scraped_text)
    
    # Filter out Ethereum addresses mistakenly caught by the broad Solana pattern
    found_sol = [addr for addr in found_sol_raw if not addr.startswith('0x') and len(addr) >= 32]
    
    unique_btc = list(set(found_btc))
    unique_eth = list(set(found_eth))
    unique_sol = list(set(found_sol))
    
    print(f"\n[+] Extraction Complete. Found {len(unique_btc)} BTC, {len(unique_eth)} ETH, and {len(unique_sol)} SOL wallets.")
    return {"btc": unique_btc, "eth": unique_eth, "sol": unique_sol}

if __name__ == "__main__":
    sample_dump = """
    Target Alpha completed payment. 1.2 BTC moved to escrow at 1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa.
    Gas fees for the malicious smart contract were loaded from 0x71C7656EC7ab88b098defB751B7401B5f6d8976F.
    The drainer script target wallet is hosted on Solana at: 7xKX17vH6ihg3wMzzv5g7890asdfghjkl123456789aB.
    """
    results = extract_crypto_wallets(sample_dump)
    print("\nResults Dictionary:", results)
