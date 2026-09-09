
# Multi-Chain Crypto OSINT Parser & Live Forensics Engine

A production-grade, local Open-Source Intelligence (OSINT) pipeline and blockchain tracking architecture designed to extract structured cryptocurrency signatures, simulate forensic heuristics, and stream live transaction telemetry directly from network nodes.

## 🚀 Engine Architecture & Capabilities

The repository is divided into three distinct operational tracking modules:

### 1. Advanced Signature Extraction (`parser.py`)
- **Multi-Chain RegEx Filters:** Automatically parses messy, unstructured text streams (scraped from illicit Telegram channels, Discord servers, and Dark Web marketplaces) to extract unique Bitcoin, Ethereum, and Solana wallet hashes.
- **WazirX Case Dataset:** Pre-loaded with actual raw intelligence streams stemming from the **July 2024 WazirX Exchange Security Breach ($235M)** to showcase automated target attribution.

### 2. Behavioral Forensic Simulator (`forensics_engine.py`)
- **Co-Spend Clustering Heuristic:** Implements the mathematical clustering algorithms utilized by firms like Chainalysis to collapse multiple distinct inputs into a single, unified threat actor profile.
- **Peeling Chain Unraveling:** Simulates a live, automated tracking loop capable of stepping forward through layered change-address hops to trace dispersed capital velocities.
- **Mixer Flagging Intercept:** Employs static smart-contract address mapping to flag transactions routing directly into privacy-obfuscation pools (e.g., Tornado Cash).

### 3. Live Web3 Network Tracker (`live_tracker.py`)
- **Direct Mainnet Node Synchronization:** Powered by the `Web3.py` library, the engine bypasses standard static database lookups to establish a direct connection with live Ethereum Mainnet RPC nodes (via the Ankr network gateway).
- **Real-Time Block Telemetry:** Automatically grabs the absolute latest mined global block number, displays current transaction throughput metrics, and continuously scans every active live transfer on the network for matching threat metrics.

---

## 📄 Case Deliverables

- **[INTELLIGENCE_REPORT.md](./INTELLIGENCE_REPORT.md):** A formal, presentation-ready Cyber Threat Intelligence (CTI) report detailing the technical Indicators of Compromise (IoCs) and behavioral forensics from the WazirX hack analysis.

---

## 🛠️ Installation & Execution

1. Clone the repository down into your isolated sandbox environment:
   ```bash
   git clone https://github.com
   cd crypto-osint-parser
   ```
2. Install the necessary Web3 dependencies:
   ```bash
   pip3 install web3
   ```
3. Run the live blockchain interceptor:
   ```bash
   python3 live_tracker.py
   ```