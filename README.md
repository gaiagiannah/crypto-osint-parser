
# Crypto Intelligence & Blockchain Forensics Pipeline (Flagship Repository)

A production-grade, unified threat intelligence orchestration architecture designed to ingest raw network data, parse indicators of compromise, simulate complex decentralized finance exploits, map relational transaction graphs, and stream live transaction telemetry directly from public blockchain network nodes.

## Centralized Command Module (`pipeline.py`)
The framework utilizes an interactive, unified console. Investigators can execute separate analytical operations seamlessly from a single terminal script:
```bash
python3 pipeline.py
```

---

## Engine Capabilities & Architecture

### 1. Basic Reconnaissance & Topological Link Analysis (`[1] CORE`)
- **Live Etherscan API Ingest:** Direct interface with Etherscan contract modules to ingest live asset execution flows.
- **Relational Network Visualization:** Utilizes `NetworkX` and `Matplotlib` to build a 300 DPI topological vector diagram (`transaction_network_map.png`), scaling transaction arrows dynamically based on transaction value size and color-coding entities (Victims, Attackers, Mixers).
- **OSINT Infrastructure Layer:** Integrated with `whois` queries to pull structural server locations and domain registration metrics instantly.
- **Market Integrity Layer:** Applies statistical Z-Score anomaly processing checks to flag pump-and-dump market anomalies.

### 2. Advanced Signature Extraction (`[2] OSINT`)
- **Multi-Chain RegEx Pipeline:** Automatically parses unformatted text strings to isolate target wallet signatures across Bitcoin, Ethereum, and Solana networks.
- **Real-World Threat Profile:** Ingests live threat reports from the **July 2024 WazirX Exchange Security Breach ($235M)** to showcase forensic attribution.

### 3. Behavioral Forensic Simulation Engine (`[3] TRACE`)
- **Co-Spend Clustering Heuristic:** Implements transaction-input clustering logic to collapse independent anonymous keys into a single threat actor entity profile.
- **Peeling Chain Unraveling:** Simulates an iterative chain tracking loop to follow obfuscated transaction perubahan as funds break into multi-layered change addresses.
- **Mixer Detection Intercept:** Identifies and scores transactions routing straight into privacy-obfuscation tools (e.g., Tornado Cash pool blocks).

### 4. Live Web3 Network Tracker (`[4] LIVE`)
- **Mainnet RPC Node Synchronization:** Employs the `Web3.py` library to construct a real-time network handshake with live Ethereum Mainnet nodes via the Ankr global gateway link.
- **Live Block Recon:** Automatically extracts block metrics, monitors live gas levels, and scans active mainnet transactions executed across the globe.

### 5. DeFi Economic Attack Emulation (`[5] DEFI`)
- **Flash-Loan Arbitrage Models:** Simulates price-oracle manipulation loops to detail how exploiters extract protocol liquidity without utilizing stolen private keys.

### 6. Cross-Ledger Bridge Relational Tracking (`[6] EDGE`)
- **Inter-Ecosystem Link-Analysis:** Models cross-chain bridge logic to match transaction parameters (timestamps, gas metrics, value equivalence) across distinct chains.

---

## Case Deliverables & Visual Assets
- **[INTELLIGENCE_REPORT.md](./INTELLIGENCE_REPORT.md):** A formal, corporate-grade Cyber Threat Intelligence report documenting indicators of compromise (IoCs) from the WazirX security hack.
- **[transaction_network_map.png](./transaction_network_map.png):** The exported 300 DPI high-resolution relational network link graph generated natively by the core canvas engine.

---

## Requirements & Quickstart
Ensure your sandbox environment contains the necessary forensic data tools:
```bash
pip3 install web3 requests pandas numpy networkx matplotlib python-whois
python3 pipeline.py
```
