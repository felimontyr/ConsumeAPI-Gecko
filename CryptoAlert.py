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
    data = response.json() #convert the response of the get to json, and convert in data to python dictionay

    if response.status_code == 200:#this if, is to confirm the status code of the request
        return data #return the dictionary of objets type crypto coin
    else:
        print(f"Error: {str(response.status_code)} in the request")#if the request status is diferent to 200, is an error

#
def sendMessageIf():
    
    cryptoValue = getCryptoPrices()#with cryptoValue get the return of def getCryptoPrices():

    binanceCoinValue = cryptoValue.get('binancecoin', {}).get('usd', 0)
    bitcoinValue = cryptoValue.get('bitcoin', {}).get('usd', 0)
    ethereumValue = cryptoValue.get('ethereum', {}).get('usd', 0)

    if binanceCoinValue > 700:#condition for send the message and use the def createMessage(nameCrypto,actualValue,maxLim):
        createMessage("binanceCoin", binanceCoinValue, 700)
    if bitcoinValue > 30000:
        createMessage("bitcoin", bitcoinValue, 30000)
    if ethereumValue > 2000:
        createMessage("ethereum", ethereumValue, 2000)

def createMessage(nameCrypto, actualValue, maxLim):

    client = Client(account_sid, auth_token)
    message_body = (f"Alert the price of {nameCrypto} has a value of {actualValue} dollars." 
                    f"The maximum limit was {maxLim} dollars.")
    
    message = client.messages.create(

        body = message_body,#mensaje de alerta creado arriba
        from_ = twilio_phone_number,
        to = whatsapp_recipient
    )
    
    print(f"send message: {message.sid}")


sendMessageIf()
