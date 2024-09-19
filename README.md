# Cryptocurrency Price Alert Script

This Python script fetches the prices of three major cryptocurrencies—Bitcoin, Ethereum, and Binance Coin—from the CoinGecko API and sends an alert via WhatsApp using the Twilio API if any of the prices exceed specified thresholds.

## Features

- Fetches real-time prices of Bitcoin, Ethereum, and Binance Coin in USD using the CoinGecko API.
- Sends a WhatsApp alert if any of the following conditions are met:
  - Bitcoin price exceeds $30,000 USD.
  - Ethereum price exceeds $2,000 USD.
  - Binance Coin price exceeds $300 USD.
- The alert message includes the cryptocurrency's name and current price, e.g., "Price Alert: The value of Bitcoin has a value of 31000 USD. The maximum limit was 30000 USD.
"

## Prerequisites

Before running the script, make sure you have the following:

1. **Python 3.12**: Ensure that Python is installed on your system. You can check this by running:
   ```bash
   python --version
   ```

2. **Twilio Account**: You will need a Twilio account to send WhatsApp messages. You can sign up for free at [Twilio's website](https://www.twilio.com/).

3. **Twilio API Credentials**: After setting up your Twilio account, gather the following credentials:
   - **Account SID**: Found in your Twilio dashboard.
   - **Auth Token**: Found in your Twilio dashboard.
   - **WhatsApp-Enabled Twilio Phone Number**: A Twilio phone number that can send WhatsApp messages.

4. **Python Libraries**: Install the required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

## API Information

1. **CoinGecko API**:
   - Endpoint: 
     ```
     https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin&vs_currencies=usd
     ```
   - This endpoint provides the prices of Bitcoin, Ethereum, and Binance Coin in USD.

2. **Twilio API**: 
   - Used to send WhatsApp messages when the price conditions are met.

## Usage Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/crypto-price-alert.git
cd crypto-price-alert
```

### 2. Configure Twilio Credentials

Before running the script, rename the `.env.rename` file and update the Twilio credentials:

```python
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+your_twilio_number'
YOUR_WHATSAPP_NUMBER = 'whatsapp:+your_phone_number'
```

### 3. Run the Script

Execute the script by running the following command in the terminal:

```bash
python crypto_alert.py
```

The script will make an HTTP request to the CoinGecko API, retrieve the prices of the cryptocurrencies, and send a WhatsApp alert if any of the thresholds are crossed.

### Example Output

If Bitcoin exceeds $30,000 USD, you might receive the following WhatsApp message:

```
Price Alert: The value of Bitcoin has a value of 31000 USD. The maximum limit was 30000 USD.
```
## Customization

You can adjust the price thresholds directly in the script by modifying the following variables:

```python
BITCOIN_THRESHOLD = 30000
ETHEREUM_THRESHOLD = 2000
BINANCECOIN_THRESHOLD = 300
```

## Troubleshooting

- Ensure that your Twilio phone number is enabled to send WhatsApp messages. Refer to [Twilio's WhatsApp documentation](https://www.twilio.com/docs/whatsapp) for setup instructions.
- If you encounter issues with the CoinGecko API, visit [CoinGecko API documentation](https://www.coingecko.com/en/api) for more details.

