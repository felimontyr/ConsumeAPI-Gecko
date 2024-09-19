#import requests 
import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
#this dates are requirment to use this python script, for alert message of twilio

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
whatsapp_recipient = os.getenv('WHATSAPP_RECIPIENT')

def getCryptoPrices():
    # use this getAction of coingecko api, for get the prices of 3 crypto coins
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin&vs_currencies=usd"
    #requests.get(url) have the information in code http
    response = requests.get(url)
    #convert the response of the get to json, and convert in data to python dictionary
    data = response.json() 
    #this if, is to confirm the status code of the request
    if response.status_code == 200:
        #return the dictionary of objets type crypto coin
        return data 
    else:
        print(f"Error: {str(response.status_code)} in the request")#if the request status is diferent to 200, is an error

def sendMessageIf():
    #with cryptoValue get the return of def getCryptoPrices()
    cryptoValue = getCryptoPrices()

    #crypto value has the info of the crypto coins and look for the keys
    #if the value of crytpo doesnt exist, the value is = 0
    binanceCoinValue = cryptoValue.get('binancecoin', {}).get('usd', 0)
    bitcoinValue = cryptoValue.get('bitcoin', {}).get('usd', 0)
    ethereumValue = cryptoValue.get('ethereum', {}).get('usd', 0)
    #condition for send the message and use the def createMessage(nameCrypto,actualValue,maxLim)
    if binanceCoinValue > 700:
        createMessage("binanceCoin", binanceCoinValue, 700)
    if bitcoinValue > 30000:
        createMessage("bitcoin", bitcoinValue, 30000)
    if ethereumValue > 2000:
        createMessage("ethereum", ethereumValue, 2000)

def createMessage(nameCrypto, actualValue, maxLim):

    client = Client(account_sid, auth_token)
    message_body = (f"Price Alert: The value of {nameCrypto} has a value of {actualValue} dollars." 
                    f"The maximum limit was {maxLim} dollars.")
    #create the message to send for recipient number
    message = client.messages.create(

        body = message_body,
        from_ = twilio_phone_number,
        to = whatsapp_recipient
    )
    
    print(f"send message: {message.sid}")

#run the script to check prices and send alerts if necessary
sendMessageIf()
