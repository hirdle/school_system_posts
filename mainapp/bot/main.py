from db import get_select_profiles, add_profile_db
from config import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(m):
    profileid = m.text[7:] 

    if get_select_profiles(profileid) == []:
        add_profile_db(profileid, m.chat.id)

    bot.send_message(m.chat.id, 'Теперь вы можете получать уведомления о новых новостях!')

def send_notify(users, text="Новая новость!"):
    
    tg_ids = []

    for i in users:
        tg_ids.append(get_select_profiles(i)[0])
    
    for i in tg_ids:
        bot.send_message(i, text)


bot.polling(none_stop=True, interval=0)