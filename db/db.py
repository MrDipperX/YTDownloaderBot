import psycopg2
from config import HOST, DATABASE_NAME, USER, PORT, PASSWORD


class PgConn:
    def __init__(self):
        self.conn = None
        try:
            self.conn = psycopg2.connect(database=DATABASE_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
            self.cur = self.conn.cursor()

        except(Exception, psycopg2.DatabaseError, psycopg2.OperationalError) as error:
            print(error)

    def create_tables(self):
        with self.conn:
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
                                    id SERIAL PRIMARY KEY NOT NULL,
                                    id_tg BIGINT ,
                                    username CHARACTER VARYING(100),
                                    temp CHARACTER VARYING(50) DEFAULT 'no',
                                    lang CHARACTER VARYING(4) DEFAULT 'ru',
                                    content_type CHARACTER VARYING(5) DEFAULT 'video',
                                    quality CHARACTER VARYING(10) NULL,
                                    last_link TEXT NULL)
                                    """)
            self.conn.commit()

    def set_user_temp(self, temp, user_id):
        with self.conn:
            self.cur.execute("UPDATE users SET temp = %s WHERE id_tg = %s;", (temp, user_id))
            self.conn.commit()

    def get_user_temp(self, user_id):
        with self.conn:
            self.cur.execute("SELECT temp FROM users WHERE id_tg = %s;", (user_id,))
            user_temp = self.cur.fetchone()
            return user_temp[0]

    def set_user_lang(self, lang, user_id):
        with self.conn:
            self.cur.execute("UPDATE users SET lang = %s WHERE id_tg = %s;", (lang, user_id))
            self.conn.commit()

    def get_user_lang(self, user_id):
        with self.conn:
            self.cur.execute("SELECT lang FROM users WHERE id_tg = %s;", (user_id,))
            user_lang = self.cur.fetchone()
            return user_lang[0]

    def get_user_info(self, user_id):
        with self.conn:
            self.cur.execute("SELECT content_type, quality, last_link FROM users WHERE id_tg = %s;", (user_id,))
            return self.cur.fetchone()

    def add_user(self, user_id, user_name):
        with self.conn:
            self.cur.execute(f"SELECT id FROM users WHERE id_tg={user_id}")
            id_data = self.cur.fetchone()
            if id_data is None:
                self.cur.execute("INSERT INTO users(id_tg, username) VALUES(%s,%s);",
                                 (user_id, user_name))
                self.conn.commit()
                return True
            return False

    def set_content_type(self, user_id, content_type):
        with self.conn:
            self.cur.execute("UPDATE users SET content_type = %s WHERE id_tg = %s;", (content_type, user_id))
            self.conn.commit()

    def set_quality(self, user_id, quality):
        with self.conn:
            self.cur.execute("UPDATE users SET quality = %s WHERE id_tg = %s;", (quality, user_id))
            self.conn.commit()

    def set_last_link(self, user_id, link):
        with self.conn:
            self.cur.execute("UPDATE users SET last_link = %s WHERE id_tg = %s;", (link, user_id))
            self.conn.commit()

