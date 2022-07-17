def send_notify(users, text="Новая новость!"):
    import sqlite3
    conn = sqlite3.connect('C:/files/projects/school_project/app/mainapp/bot/users.db', check_same_thread=False)
    import telebot

    def get_select_profiles(id):
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM users WHERE profileid={id}")
        all_result = cur.fetchall()
        return all_result

    bot = telebot.TeleBot("5430611437:AAEe6A-QOZK-tkjX7pSj0GmM39Qd9lt41gQ")
    
    tg_ids = []

    for i in users:
        if get_select_profiles(i) != []:
            tg_ids.append(get_select_profiles(i)[0][2])

    for i in tg_ids:
        bot.send_message(i, text)
    