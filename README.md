<div align="center">

<img src="https://i.top4top.io/p_3536m9kq01.png" alt="Facebook Brute Force" width="800" />

<br/>
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=22&pause=1200&center=true&vCenter=true&random=false&width=750&lines=Facebook+Brute+Force+Tool;HTTP%2FS+Proxy+Support+%7C+Auto+Retry+%7C+Telegram+Alerts;Multi-threaded+%7C+Fast+%7C+Robust" alt="Typing SVG" /></a>

<br/>

<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white"></a>
<img alt="OS" src="https://img.shields.io/badge/OS-Windows%20%7C%20Linux-555555?logo=windows&logoColor=white">
<img alt="Proxies" src="https://img.shields.io/badge/Proxy-HTTP%2FHTTPS-blue?logo=cloudflare&logoColor=white">
<img alt="Threads" src="https://img.shields.io/badge/Threads-Configurable-orange">
<img alt="Telegram" src="https://img.shields.io/badge/Telegram-Alerts-2CA5E0?logo=telegram&logoColor=white">

</div>

---

## Overview
A robust, multi-threaded Facebook brute force tool built for research and educational demonstrations. It automates credential attempts, handles HTTP/S proxies intelligently, and implements a strict rate-limit strategy that re-checks blocked accounts instead of skipping them.

## Highlights
- **Smart Rate-Limit Handling:** Re-checks temporarily blocked accounts after backoff instead of discarding them.
- **Resilient Proxy Flow:** Keeps trying until a working HTTP/S proxy is found; doesn’t skip accounts due to dead proxies.
- **Multi-Threaded Engine:** User-defined threads for higher throughput with safe queue processing.
- **Real-time Telemetry:** Optional Telegram alerts for successful or secure (checkpointed) logins.
- **Structured Outputs:** Results saved under `cathack_Facebook_BruteForce/` as they occur.

## Requirements
- Python 3.8+
- `requests`, `colorama` (install via `requirements.txt`)
- Combo file: one `email:password` per line
- Proxy file: HTTP/S proxies, one per line (see formats below)
- Optional: `TELEGRAM_BOT.json` for alerts

## Table of Contents
- [Overview](#overview)
- [Highlights](#highlights)
- [Requirements](#requirements)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Combo & Proxy Formats](#combo--proxy-formats)
- [Usage Flow](#usage-flow)
- [Outputs](#outputs)
- [Troubleshooting](#troubleshooting)
- [Disclaimer](#disclaimer)
- [Support](#support)

## Installation
```bash
# 1) Clone
git clone https://github.com/vv1ck/Brute-Force-Facebook.git
cd Brute-Force-Facebook

# 2) (Optional) Create venv
# Windows (PowerShell)
python -m venv venv
./venv/Scripts/Activate.ps1

# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# 3) Install dependencies
pip install -r requirements.txt
```

## Quick Start
```bash
# From repository root
python BruteForce-facebook.py
```
Follow the prompts to provide:
- Combo file path
- Proxy file path
- Number of threads
- Telegram `ID` and `TOKEN` (or ensure `TELEGRAM_BOT.json` exists)

## Combo & Proxy Formats
- Combo file (required):
```text
email@example.com:password123
user@example.com:qwerty2024
```
- Proxy file (HTTP/S supported):
```text
http://127.0.0.1:8080
https://127.0.0.1:8443
http://user:pass@host:port
```
Notes:
- Proxies are randomly rotated. The tool persists until a working proxy is found.
- If a proxy fails, the account is NOT skipped; the attempt is re-tried.

## Usage Flow
1) Tool loads combo list into a queue.  
2) You provide a proxy list and set thread count (large values are capped for stability).  
3) For each account, the tool:
   - Picks a proxy at random.
   - Attempts login using the mobile Graph endpoint.
   - Interprets responses: `success` → token logged; `secure`/checkpoint → recorded; invalid → increments failure stats; `rate_limit` → backoff and re-check.
4) Telegram alerts (if configured) are sent on `success` or `secure` cases.

## Outputs
Files are written to `cathack_Facebook_BruteForce/`:
- `Hacked.txt` — email:password with access token
- `Secure.txt` — email:password requiring verification/checkpoint
- `error.txt` — responses and unexpected errors for later review

## Troubleshooting
- Dead proxies / timeouts: Provide a larger, fresher proxy list. HTTP/S supported.
- High rate-limit counter: Reduce threads or wait; tool re-checks blocked accounts automatically.
- No Telegram alerts: Verify `TELEGRAM_BOT.json`:
```json
{
  "ID": "123456789",
  "TOKEN": "123456789:AA..."
}
```
- Output folder missing: It is auto-created as `cathack_Facebook_BruteForce/`.

## Disclaimer
This repository is for educational and research purposes only. Unauthorized use against accounts you do not own is illegal and unethical. You, not the authors or maintainers, are solely responsible for how you use this code.

---

## Support
Support me with a cup of coffee:  
Usdt Tron (TRC20) : TJV9c9PbvBcY86LTnWUrfSenoywye1WHJL
Litecoin: Lg8Njr8G8VdrgFrXQvwRRr1ctqAB4iLmyS
