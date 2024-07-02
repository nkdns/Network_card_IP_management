import sqlite3,os

class ql():
    def __init__(self) -> None:
        programdata = os.getenv('ProgramData')
        dbfile = programdata + '\cn.nkdns.netipchange'
        if not os.path.exists(dbfile):
            os.makedirs(dbfile)
        self.sqlconnect = sqlite3.connect(dbfile + '\main.db')
        self.sqlcursor = self.sqlconnect.cursor()
        self.checktable()

    def checktable(self) -> None:
        table_name = 'IPinfo'
        self.sqlcursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        if self.sqlcursor.fetchone()[0] == 0:
            self.sqlcursor.execute('''CREATE TABLE IPinfo
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        IP TEXT,
                        NetMask TEXT,
                        Remarks TEXT)''')
            print(f"表 '{table_name}' 创建成功.")
        else:
            print(f"表 '{table_name}' 存在.")
        self.sqlconnect.commit()

        table_name = 'config'
        self.sqlcursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        if self.sqlcursor.fetchone()[0] == 0:
            self.sqlcursor.execute('''CREATE TABLE config
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        LastInterface TEXT,
                        WithOutVM TEXT)''')
            query = 'INSERT INTO config (LastInterface, WithOutVM) VALUES (?, ?)'
            self.I_U_D(query,('',''))
            print(f"表 '{table_name}' 创建成功.")
        else:
            print(f"表 '{table_name}' 存在.")
        self.sqlconnect.commit()
    
    def select(self,query,body=()):
        self.sqlcursor.execute(query,body)
        results = self.sqlcursor.fetchall()
        return results
    
    def I_U_D(self,query,body=None):
        self.sqlcursor.execute(query,body)
        self.sqlconnect.commit()

    def __del__(self):
        self.sqlcursor.close()
        self.sqlconnect.close()
        