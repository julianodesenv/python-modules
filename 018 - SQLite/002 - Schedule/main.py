import sqlite3

"""
conn = sqlite3.connect('018 - SQLite/002 - Schedule/schedule.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS schedule ('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,' 
                'name TEXT,'
                'phone TEXT'
            ')')

cursor.close()
conn.close()
"""

class ScheduleDB:
    def __init__(self, file):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()

    def create(self, name, phone):
        consulta = 'INSERT OR IGNORE INTO schedule (name, phone) VALUES (?, ?)'
        self.cursor.execute(consulta, (name, phone))
        self.conn.commit()

    def edit(self, name, phone, id):
        consulta = 'UPDATE OR IGNORE schedule SET name=?, phone=? WHERE id=?'
        self.cursor.execute(consulta, (name, phone, id))
        self.conn.commit()

    def destroy(self, id):
        consulta = 'DELETE FROM schedule WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def list(self):
        self.cursor.execute('SELECT * FROM schedule')

        for linha in self.cursor.fetchall():
            print(linha)

    def search(self, valor):
        consulta = 'SELECT * FROM schedule WHERE name LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))

        for line in self.cursor.fetchall():
            print(line)

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    schedule = ScheduleDB('schedule.db')
    #schedule.search('juliano')
    schedule.create('juliano', '11111')