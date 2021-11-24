from  telegram_bot import bot


# -----Bot-----
bot_token = ''  # токен бота
# -----Bitcoin-----
address = ''  # адрес в блокчейн сети 
# -----BotKeyboard-----
keyboard_main = {
    'reply_markup' : {'keyboard' : 
        [
            [{'text' : 'Баланс'}],
            [{'text' : 'Курс'}]
        ],
    'resize_keyboard' : True,
    'one_time_keyboard' : True
    }
}

keyboard_balance = {
    'chat_id' : bot(bot_token).get_chat_id(),
    'text' : 'None',
    'reply_markup' : {'keyboard':
        [
            [{'text' : '$'}],
            [{'text' : 'B'}],
            [{'text' : 'Назад'}]
        ],
    'resize_keyboard' : True,
    }
}
