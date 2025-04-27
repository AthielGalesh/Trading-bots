import os, time, requests, psutil

from globals import BOT_TOKEN, CHAT_ID


def send_message(message):
    bot_path = BOT_TOKEN  #USE YOUR CUSTOM CREDENTIALS, IMPORT THEM FROM GLOBALS
    chat_url = CHAT_ID
    telegram_url = "https://api.telegram.org/bot"
    text_url = f'&text={message}'
    final_url = telegram_url + bot_path + chat_url + text_url
    response = requests.get(final_url)
    assert response.status_code == 200, f"Error: {response.status_code}"

#testing telegram bot

send_message("Hello Telegram from Python!")

while True:
    time.sleep(5)
    msg = "the cpu usage is {}%".format(psutil.cpu_percent(interval=4))
    send_message(msg)
