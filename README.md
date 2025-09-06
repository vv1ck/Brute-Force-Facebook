![Brute Force Tool](https://i.top4top.io/p_3536m9kq01.png)  

# Facebook Brute Force Tool

## Overview
This tool is designed to perform brute force attacks on Facebook accounts by automating the process of trying multiple username and password combinations. It is equipped with advanced features to handle rate limits and proxy management effectively.

## Features
- **Rate Limiting:** Automatically retries checking blocked accounts after a specified interval.
- **Proxy Management:** Supports HTTP/S proxies and continues attempts until a working proxy is found.
- **Detailed Logging:** Logs successful, secure, and error attempts for easy monitoring.
- **Telegram Notifications:** Sends notifications of successful or secure attempts to a specified Telegram account.

## Requirements
- **Combo File:** A text file containing a list of usernames and passwords.
- **Proxy File:** A text file containing a list of HTTP/S proxies.
- **Telegram Setup:** A `TELEGRAM_BOT.json` file containing your Telegram ID and Token for notifications.
- **Python Libraries:** Ensure the following libraries are installed: `requests`, `colorama`, `datetime`, `threading`, `queue`.

## Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/vv1ck/Brute-Force-Facebook.git
   cd facebook-bruteforce-tool
   ```

2. **Install Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Files:**
   - Create a combo file with your target usernames and passwords.
   - Create a proxy file with your proxy list.
   - Ensure you have a `TELEGRAM_BOT.json` file with your Telegram credentials.

4. **Run the Tool:**
   - Execute the script using Python: `python BruteForce-facebook.py`
   - Follow the on-screen instructions to input your combo and proxy files.

5. **Monitor Results:**
   - Check the output files in the `cathack_Facebook_BruteForce` directory for results.
   - Successful attempts will be logged in `Hacked.txt` and secure attempts in `Secure.txt`.

## Usage
- **Combo File Input:** Enter the path to your combo file when prompted.
- **Proxy File Input:** Enter the path to your proxy file when prompted.
- **Telegram Notifications:** Ensure your Telegram ID and Token are correctly set up in `TELEGRAM_BOT.json` to receive notifications.

## Disclaimer
This tool is intended for educational purposes only. Unauthorized use of this tool is illegal and unethical. The author is not responsible for any misuse or damage caused by this tool.
