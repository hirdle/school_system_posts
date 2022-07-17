import sqlite3
conn = sqlite3.connect('C:/files/projects/school_project/app/mainapp/bot/users.db', check_same_thread=False)

# userid, profileid, telegramid

# cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS users(
#    userid INTEGER PRIMARY KEY AUTOINCREMENT NULL,
#    profileid INTEGER NULL,
#    telegramid INTEGER NULL);
# """)

def get_select_profiles(id):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE profileid={id}")
    all_result = cur.fetchall()
    return all_result

def add_profile_db(profileid, telegramid):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO users (profileid, telegramid) VALUES('{profileid}','{telegramid}');", )
    conn.commit()