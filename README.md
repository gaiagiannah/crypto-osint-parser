# Crypto OSINT Regex Parser

A lightweight, local Open-Source Intelligence (OSINT) pipeline designed to extract structured cryptocurrency wallet signatures from raw, unformatted text files scraped from illicit Telegram channels, Discord servers, and Dark Web marketplaces.

## Features
- **Multi-Chain Asset Parsing:** Detects Bitcoin (Legacy & SegWit), Ethereum, and Solana addresses automatically.
- **Deduplication:** Sanitizes messy data streams to compile unique target profiles.
- **Heuristic Filtering:** Bypasses false-positive pattern overlaps between multi-chain structures.

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate into the directory and execute:
   ```bash
   python parser.py
   ```
