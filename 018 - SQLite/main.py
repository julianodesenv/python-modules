import sqlite3

conn = sqlite3.connect('018 - SQLite/base.db')
cursor = conn.cursor()

"""
cursor.execute('CREATE TABLE IF NOT EXISTS clients('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,' 
                'name TEXT'
            ')')


cursor.execute('INSERT INTO clients (name) VALUES ("Juliano Monteiro")')
conn.commit()

#cursor.execute('INSERT INTO clients (name) VALUES (?)', ('Name 002'))
cursor.execute('INSERT INTO clients (name) VALUES (:name)', {'name': 'Name 003'})
cursor.execute('INSERT INTO clients VALUES (:id, :name)', {'id': None, 'name': 'Name 004'})
"""

conn.commit()

#cursor.execute('UPDATE clients SET name=:name WHERE id=:id', {'id': 2, 'name': 'Juliano'})
#cursor.execute('DELETE FROM clients WHERE id=:id', {'id': 2})
cursor.execute('SELECT * FROM clients WHERE name = :name', {'name': 'Name 003'})
#cursor.execute('SELECT * FROM clients')

for line in cursor.fetchall():
    print(line)

cursor.close()
conn.close()