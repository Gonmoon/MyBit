from  telegram_bot import bot
from bitcoin import bitcoin
from config import *


# -----Main-----
update_id = None
bot = bot(bot_token)
# -----Запуск-----
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
                if message == 'Баланс':
                    bot.send_sticker('CAACAgIAAxkBAAICe2GebDRgv6BWXWIQmSLyo46ZZZo8AAKZAQAC5H1bFt9b4c7myeq7IgQ')
                    bot.send_message_with_json('Выберите валюту', keyboard_balance)
                elif message == '$':
                    bot.send_sticker('CAACAgIAAxkBAAICcmGearGmGGJx8XpTomxddARhF2wEAAItFAACNgawSCxcMGGByOZ8IgQ')
                    bot.send_message(bitcoin(address).get_balance()[1])
                elif message == 'B':
                    bot.send_sticker('CAACAgIAAxkBAAICc2GearJA1I6WKXG3Owkjl4xfkqGNAAKFDwACnHjoSPqenYYek08FIgQ')
                    bot.send_message(bitcoin(address).get_balance()[0])
                elif message == 'Курс':
                    bot.send_sticker('CAACAgIAAxkBAAICkGGebMWdqQMUbnyH-V9XZZcetxVKAAKcEAACJVxASGelRM-c9WNoIgQ')
                    bot.send_message_with_json(bitcoin(address).get_balance()[2], keyboard_main)
                elif message == 'Назад':
                    bot.send_message_with_json('Удачной работы!', keyboard_main)
                    bot.send_sticker('CAACAgIAAxkBAAICeGGea6_hXBRVSxdWIS8UcfkQVDd-AAKSFAAChnVIS1tKdPMPYallIgQ')
                elif message == '/start':
                    bot.send_message_with_json('Добро пожаловать!', keyboard_main)
                    bot.send_sticker('CAACAgIAAxkBAAICd2Gea5wYKszMKQsEdJ2e0Iacns4WAAJcFAACzWlISz82ySdCb60UIgQ')
            except:
                message = None
