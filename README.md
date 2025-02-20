# Gram_group_joiner

<img src="https://raw.githubusercontent.com/spmedia/Telegram-Channel-Joiner/main/wizard3.jpg" style="width: 75%; height: 75%" />

A Python bot utilizing the [Pyrogram API Framework](https://docs.pyrogram.org/) to automate the process of joining a list of Telegram channels and groups. This tool is designed to aid CTI and OSINT practitioners in efficiently managing their sock puppet accounts.

### Features:
- **Account Limits**: Supports both free (500 channels/groups max) and Telegram Premium accounts (1000 channels/groups max).
- **API Credentials**: Obtain your API ID and hash from [my.telegram.org](https://my.telegram.org/).
- **Channel/Group List**: Handles lists of Telegram channels and groups.
- **Private Channels**: To join private channels, modify line 34 and uncomment line 35 in the script.
- **Rate Limiting**: Implements a random delay (300-600 seconds) between joins to avoid rate limits. 

### Installation:
```sh
python3 -m pip install pyrogram tgcrypto
