# Load credentials from .env file
from dotenv import load_dotenv
load_dotenv()

import os
TOKEN = os.getenv('TOKEN')

# ---- Bot ----
import requests
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

# Get all chats
result = requests.get(url).json() 
print( result ) 

# Retrieve chat ID (needed to send messages)
chat_id = result['result'][0]['message']['chat']['id']
print( f"\n  CHAT ID: {chat_id}" )

# Send message
message = "hello from your telegram bot 2"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print( f"Send result: {requests.get(url).json()} ") # this sends the message