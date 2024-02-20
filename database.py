import sqlite3

class Database:
    def __init__(self):
        # build short.db if not exist
        connection = sqlite3.connect("short.db")
        curs = connection.cursor()
        curs.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='SHORTURL'")
        temp_result = curs.fetchone()
        
        if temp_result is None:
            curs.execute("CREATE TABLE SHORTURL \
            		(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            		SHORT TEXT NOT NULL, \
            		COMPLETE TEXT NOT NULL)")
            connection.commit()
            print("CREATED TABLE")
        else:
            print("using existing table")
        curs.close()
        connection.close()

    def insert(self, url, short_url):
        connection = sqlite3.connect("short.db")
        curs = connection.cursor()
        curs.execute("SELECT ID, SHORT, COMPLETE FROM SHORTURL")
        for row in curs:
            if row[1] == short_url:
                # print("ABORT")
                return None
            elif row[2] == url:
                # print("ABORT")
                return row[1]
        cmd = f"INSERT INTO SHORTURL (SHORT, COMPLETE) VALUES ('{short_url}', '{url}')"
        # print(cmd)
        curs.execute(cmd)
        connection.commit()
        curs.close()
        connection.close()
        return short_url

    def get_url(self, short_url):
        connection = sqlite3.connect("short.db")
        curs = connection.cursor()
        cmd = f"SELECT COMPLETE FROM SHORTURL WHERE SHORT='{short_url}'"
        # print(cmd)
        curs.execute(cmd)
        ret = curs.fetchone()
        curs.close()
        if ret is None:
            return None
        return ret[0]


if __name__ == "__main__":
    db = Database()
    db.insert("github.com", "abc")
    db.insert("kk.com", "def")
    db.insert("github.com", "xyz")
    print(db.get_url("abc"))
    print(db.get_url("xyz"))
    print(db.get_url("def"))