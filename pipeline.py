
import os
import sys
import time
import requests
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import whois
from datetime import datetime

# =========================================================================
# PILLARS 1-4: YOUR ORIGINAL FORENSIC PIPELINE ENGINE (PRESERVED NATIVELY)
# =========================================================================

def analyze_market_anomalies(df):
    print("\n [MARKET INTEGRITY LAYER] Auditing Trading Patterns for Anomalies...")
    if df.empty or len(df) < 2:
        return
    mean_volume = df["Amount"].mean()
    std_volume = df["Amount"].std() if df["Amount"].std() != 0 else 1
    anomalies_detected = False
    for idx, row in df.iterrows():
        z_score = (row["Amount"] - mean_volume) / std_volume
        if z_score > 1.5:
            anomalies_detected = True
            print(f"  PUMP ANOMALY DETECTED | Z-Score: {z_score:.2f}")
            print(f"   ↳ Size: {row['Amount']:,.2f} Tokens | Hash: {row['Hash'][:10]}...")
    if not anomalies_detected:
        print(" [+][+] Market Integrity Check Clear.")
    print("-----------------------------------------------------------------")

def perform_osint_domain_lookup(domain_name):
    print(f"\n [OSINT LAYER] Launching Infrastructure Audit on: {domain_name}...")
    try:
        domain_info = whois.whois(domain_name)
        print(" --- INFRASTRUCTURE INTELLIGENCE SUMMARY ---")
        print(f"Registrar:      {domain_info.registrar}")
        print(f"Server Location: {domain_info.whois_server}")
        print("---------------------------------------------")
    except Exception:
        print(" [-] OSINT Lookup Failed.")

def generate_local_intelligence_data():
    print(" --- STANDBY: ACTIVATING LOCAL DATA SIMULATION MATRIX ---")
    mock_data = [
        {"Timestamp": datetime.now(), "Sender": "0xVictim_Wallet", "Receiver": "0xBurner_Wallet_A", "Amount": 85000.0, "Hash": "0xabc123..."},
        {"Timestamp": datetime.now(), "Sender": "0xSuspect_Alpha", "Receiver": "0xBurner_Wallet_A", "Amount": 12000.0, "Hash": "0xdef456..."},
        {"Timestamp": datetime.now(), "Sender": "0xBurner_Wallet_A", "Receiver": "0xHighRisk_Mixer", "Amount": 145000.0, "Hash": "0xghi789..."},
        {"Timestamp": datetime.now(), "Sender": "0xRegular_User", "Receiver": "0xMerchant_Node", "Amount": 450.0,   "Hash": "0xjkl012..."},
        {"Timestamp": datetime.now(), "Sender": "0xWhale_Holder", "Receiver": "0xSuspect_Alpha", "Amount": 31000.0, "Hash": "0xmno345..."}
    ]
    return pd.DataFrame(mock_data)

def run_original_forensic_pipeline(contract_address, target_domain):
    api_key = "2N8YQ4Y96A9IFFKEA7PTG1DTUFZIAWUPGK"
    url = "https://etherscan.io"
    params = {"module": "account", "action": "tokentx", "contractaddress": contract_address, "page": 1, "offset": 100, "sort": "desc", "apikey": api_key}
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        if data["status"] != "1" or data["message"] == "NOTOK":
            df = generate_local_intelligence_data()
        else:
            tx_list = []
            for tx in data["result"]:
                decimals = int(tx.get("tokenDecimal", 18))
                tx_list.append({
                    "Timestamp": datetime.fromtimestamp(int(tx["timeStamp"])),
                    "Sender": tx["from"][:8] + "..",
                    "Receiver": tx["to"][:8] + "..",
                    "Amount": float(tx["value"]) / (10 ** decimals),
                    "Hash": tx["hash"]
                })
            df = pd.DataFrame(tx_list)
    except Exception:
        df = generate_local_intelligence_data()

    print("\n Constructing Production-Grade Link Analysis Diagram...")
    G = nx.DiGraph()
    for idx, row in df.iterrows():
        G.add_edge(row["Sender"], row["Receiver"], weight=row["Amount"])
    
    fig, ax = plt.subplots(figsize=(12, 9), facecolor='#111111')
    ax.set_facecolor('#111111')
    pos = nx.circular_layout(G)
    
    color_map = []
    for node in G.nodes():
        node_lower = node.lower()
        if "victim" in node_lower: color_map.append("#32CD32")
        elif "suspect" in node_lower or "burner" in node_lower: color_map.append("#FF4500")
        elif "mixer" in node_lower: color_map.append("#FFD700")
        else: color_map.append("#1F78B4")
            
    weights = [G[u][v]['weight'] for u, v in G.edges()]
    max_weight = max(weights) if weights else 1
    edge_widths = [1.0 + (w / max_weight) * 5.0 for w in weights]
    
    nx.draw_networkx_nodes(G, pos, node_size=2200, node_color=color_map, alpha=0.9, ax=ax)
    nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color="#CCCCCC", alpha=0.4, 
                           arrowsize=18, arrowstyle='->', connectionstyle="arc3,rad=0.15", ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=9, font_family="sans-serif", font_weight="bold", font_color="#FFFFFF", ax=ax)
    
    plt.title("FORENSIC EVIDENCE: TOPOLOGICAL LINK ANALYSIS", color="#FFFFFF", fontsize=16, fontweight="bold", pad=20)
    plt.text(0.5, -0.05, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | Network context: Ethereum Mainnet Ledger", 
             color="#888888", fontsize=9, ha="center", transform=ax.transAxes)
    
    plt.axis("off")
    plt.tight_layout()
    
    output_filename = "transaction_network_map.png"
    plt.savefig(output_filename, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    
    print(f" [+][+] SUCCESS: Professional graphics matrix exported as '{output_filename}'!")
    perform_osint_domain_lookup(target_domain)
    analyze_market_anomalies(df)


# =========================================================================
# ORCHESTRATION LAYER: COUPLING NEW INTEL SHURIKENS
# =========================================================================

try:
    import parser as osint_parser
    import live_tracker as network_tracker
    import forensics_engine as simulator
    import defi_simulator as defi_engine
    import bridge_tracker as bridge_engine
except ImportError as e:
    print(f"[-] Pipeline Sub-Module Notice: {e}")

def display_unified_menu():
    print("\n" + "="*70)
    print(" CRYPTO THREAT INTELLIGENCE & FORENSICS PIPELINE MASTER NODE")
    print("="*70)
    print(" [1] [CORE] Run original Etherscan API Link Graph & Infrastructure Scan")
    print(" [2] [OSINT] Run Raw Text Regex Signature Parser (WazirX Dataset)")
    print(" [3] [TRACE] Run Behavioral Forensics (Clustering, Peeling Chains)")
    print(" [4] [LIVE]  Launch Live Ethereum Block Interceptor (Web3.py Node)")
    print(" [5] [DEFI]  Execute Flash-Loan Arbitrage Exploit Simulator")
    print(" [6] [EDGE]  Execute Cross-Chain Bridge Asset Link Tracer")
    print(" [7] Exit Cyber Forensics Console")
    print("======================================================================")

def main_orchestrator():
    USDC_SMART_CONTRACT = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
    SUSPICIOUS_DOMAIN = "incadigital.com" 

    while True:
        display_unified_menu()
        try:
            choice = input("Select an automated workflow utility [1-7]: ").strip()
        except KeyboardInterrupt:
            print("\n[-] Pipeline closed down safely via operator request.")
            sys.exit(0)
            
        if choice == "1":
            run_original_forensic_pipeline(USDC_SMART_CONTRACT, SUSPICIOUS_DOMAIN)
        elif choice == "2":
            sample_dump = osint_parser.wazirx_intel_dump if hasattr(osint_parser, 'wazirx_intel_dump') else ""
            osint_parser.extract_crypto_wallets(sample_dump)
        elif choice == "3":
            inputs = ["0xHackerWallet_A", "0xHackerWallet_B", "0xHackerWallet_C"]
            simulator.simulate_wallet_clustering(inputs)
            simulator.trace_peeling_chain(10.0, "0xRoot_Hacker_Vault")
        elif choice == "4":
            w3 = network_tracker.connect_to_live_ethereum()
            if w3: network_tracker.scan_latest_live_block(w3)
        elif choice == "5":
            defi_engine.simulate_flash_loan_exploit(10000000, "MangoMarket_Exploit_Clone")
        elif choice == "6":
            bridge_engine.track_cross_chain_jump("Ethereum_Mainnet", "Solana_Network", "0x9f8e7d6c5b4a3210")
        elif choice == "7":
            print("\n[*] Shutting down intelligence core. Connection closed.")
            break
        else:
            print("[-] Selector parsing error: Choose a parameter within [1-7].")
            
        input("\n[Press Enter to return to main framework selection...]")

if __name__ == "__main__":
    main_orchestrator()
