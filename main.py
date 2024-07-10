import os
import requests
from dotenv import load_dotenv


def get_updates(token):
    """Retrieve updates from the Telegram bot."""
    url = f"https://api.telegram.org/bot{token}/getUpdates"
    response = requests.get(url).json()
    return response

def send_message(token, chat_id, message):
    """Send a message to a specific chat using the Telegram bot."""
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    response = requests.get(url).json()
    return response



if __name__ == "__main__":
    # Load the token
    load_dotenv()
    TOKEN = os.getenv('TOKEN')

    # Retrieve updates
    updates = get_updates(TOKEN)
    print(updates)

    # Retrieve chat ID
    chat_id = updates['result'][0]['message']['chat']['id']
    print(f"\n  CHAT ID: {chat_id}")

    # Send a message
    message = "hello from your telegram bot 2"
    send_result = send_message(TOKEN, chat_id, message)
    print(f"Send result: {send_result}")
