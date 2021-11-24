import requests
import json


class bot():
    def __init__(self, bot_token):
        # -----создание url бота-----
        self.url = 'https://api.telegram.org/bot' + bot_token
        self.bot_token = bot_token
           
    def get_updates(self, offset=None):
        # -----получения обновления-----
        url = self.url + "/getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        return json.loads(requests.get(url).content)
    
    def get_chat_id(self):
        # -----получения id чата-----
        id = None
        answer = json.loads(requests.get(self.url + '/getUpdates').content)
        answer = answer["result"]
        for item in answer:
            id = item["message"]["chat"]["id"]
        return id
    
    def send_message(self, text):
        # -----отправка сообщения-----
        requests.post('{0}/sendMessage?chat_id={1}&text={2}'.format(self.url,
        bot(self.bot_token).get_chat_id(), text))

    def send_message_with_json(self, text, json):
        # -----отправка сообщения с json-----
        requests.post('{0}/sendMessage?chat_id={1}&text={2}'.format(self.url,
        bot(self.bot_token).get_chat_id(), text), json=json)

    def send_sticker(self, sticker):
        # -----отправка стикера-----
        requests.post('{0}/sendSticker?chat_id={1}&sticker={2}'.format(self.url,
        bot(self.bot_token).get_chat_id(), sticker))
     