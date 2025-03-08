# Wi-Fi Password Cracker (WPA3)

## Description
This project is a Python script designed to scan available Wi-Fi networks and attempt to crack the password of a selected network using a brute-force approach. The script uses the `pywifi` library to handle Wi-Fi connections and automates password attempts using multithreading.

## Features
- Scans for available Wi-Fi networks and displays their signal strength.
- Allows the user to select a target network.
- Generates and tests passwords using a predefined character set.
- Uses multithreading to optimize speed.
- Supports WPA3 encryption.

## Requirements
- Python 3.6+
- `pywifi` library
- Administrator privileges to manage network profiles

## Installation
1. Install Python if not already installed.
2. Install the required dependencies using pip:
   ```sh
   pip install pywifi
   ```
3. Run the script with administrator privileges:
   ```sh
   python script.py
   ```

## Usage
1. The script will scan for available Wi-Fi networks.
2. Select a network by entering its corresponding number.
3. The script will generate and attempt passwords until the correct one is found.
4. If a valid password is discovered, it will be displayed on the screen.

## Disclaimer
This tool is intended for educational and security testing purposes only. Unauthorized access to Wi-Fi networks is illegal and unethical. Use this script only on networks you own or have explicit permission to test.

**By 4RT0R14S**

