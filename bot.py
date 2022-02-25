import requests
import misc
import json
from yobit import get_btc
from time import sleep

global last_update_id
last_update_id = 0

token = misc.TOKEN
URL = 'https://api.telegram.org/bot' + token +'/'

# https://api.telegram.org/bot5159164746:AAEg9Mly6V3hfjWm-to1PJFwBVvXIpSiCOg/sendmessage?chat_id=182325625&text=hi

def get_updates(): # формируем словать
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message(): # абираем из него нужное
    d = get_updates()
    last_object = d['result'][-1]
    current_update_id = last_object['update_id']
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object['message']['chat']['id']
        message_text = last_object['message']['text']
        message = {
            'chat_id': chat_id,
            'text': message_text
        }
        return message
    return None


def send_message(chat_id, text='bazaaaa'): #отправляем сообщеньку
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

def main():
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            if text == '/btc':
                send_message(chat_id, get_btc())
        else:
            continue
        sleep(3)

if __name__ == '__main__':
    main()