import os
import requests
from dotenv import load_dotenv

def load_bot_token_from_os() -> str:
    """Loads the Telegram API Token from local .env file."""
    load_dotenv()
    return os.getenv('TOKEN')

def get_message_updates(token:str):
    """
    Retrieve messages from Telegram bot.
    
    PARAMETERS
        token: Telegram Bot Token
    """
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url).json()
    return response

def get_chat_id_from_message_response(message_json:str):
    try:
        chat_id = message_json['result'][0]['message']['chat']['id']
    except: 
        raise Exception("Error: Unable to retrieve chat ID from message response. Maybe dict keys changed.")
        chat_id = None

    return chat_id


def send_message(token:str, chat_id:int, message:str):
    """
    Send a message to a specific chat using the Telegram bot.
    
    PARAMETERS
        token: Telegram Bot Token
        chat_id:  ID of the specific private chat or group chat. Get ID from results or xxxxxxxx
        message: Message text. Supports Markdown.
    """
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=MarkdownV2"
    response = requests.get(url).json()
    return response

if __name__ == "__main__":
    # Load the token
    TOKEN = load_bot_token_from_os()

    # Retrieve updates
    updates = get_message_updates(TOKEN)
    print(updates)
    print("-----------")

    # Retrieve chat ID
    chat_id = get_chat_id_from_message_response(updates)
    print(f"\n  CHAT ID: {chat_id}")

    # Send a message
    message = "hello from your telegram bot 3\\. Dots have to be escaped in markdown mode\\! *Bold text*  __underline__   _italic text_"
    send_result = send_message(TOKEN, chat_id, message)
    print(f"Send result: {send_result}")
