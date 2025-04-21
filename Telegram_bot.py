import os, time, requests, psutil
from dotenv import load_dotenv




#CREDENTIALS
BOT_TOKEN = Telegram_bot_token #Place your telegram values here
CHAT_ID = Chat_id_value




class Telegram_Mensaje:
    def send_telegram(self, message="test"):
        telegram_url = "https://api.telegram.org"
        bot_path = f"/bot{BOT_TOKEN}"
        chat_url = f"/sendMessage?chat_id={CHAT_ID}"
        text_url = f"&text={message}"
        final_url = telegram_url + bot_path + chat_url + text_url
        response = requests.get(final_url)
        assert response.status_code == 200

#you can also check your device if you are running your own server, for example:
while True:
    time.sleep(5)
    msg = "the cpu usage is {}%".format(psutil.cpu_percent(interval=4))
    send_telegram(msg)
