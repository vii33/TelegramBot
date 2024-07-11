import pytest
import os
from telegram_bot import load_bot_token_from_os, get_message_updates, send_message, get_chat_id_from_message_response


@pytest.fixture
def token():
    """Load the token from the environment."""
    return load_bot_token_from_os()


def test_get_updates(token):
    result = get_message_updates(token)
    
    assert 'ok' in result and result['ok'] is True
    assert 'result' in result
    assert isinstance(result['result'], list)

def test_get_chat_id_from_message_response_valid_json():
    # Test case 1: Valid JSON response
    valid_json = {'result': [ {'message': {'chat': {'id': 123456789} } } ]  }
    chat_id = get_chat_id_from_message_response(valid_json)
    assert chat_id == 123456789

def test_get_chat_id_from_message_response_invalid_json():
    # Test case 2: Invalid JSON response
    invalid_json = '{"invalid": "json"}'
    with pytest.raises(Exception) as exc_info:
        get_chat_id_from_message_response(invalid_json)
    assert str(exc_info.value) == "Error: Unable to retrieve chat ID from message response. Maybe dict keys changed."


def test_send_message(token):
    updates = get_message_updates(token)
    assert 'result' in updates
    assert len(updates['result']) > 0
    
    chat_id = updates['result'][0]['message']['chat']['id']
    message = "Unit Test Message"
    
    send_result = send_message(token, chat_id, message)
    
    assert 'ok' in send_result and send_result['ok'] is True
    assert 'result' in send_result
    assert 'message_id' in send_result['result']
