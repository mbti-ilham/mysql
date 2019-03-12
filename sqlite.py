import sqlite3
#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT,
age INTEGER
)
""")
conn.commit()
cursor.execute("""INSERT INTO users(name, age) VALUES(?, ?)""",
("olivier", 30))
conn.commit()


data = {"name" : "clara", "age" : 31}
cursor.execute("""INSERT INTO users(name, age) VALUES(:name, :age)""", data)
conn.commit()

id1 = cursor.lastrowid
print('dernier id: %d' % id1)

users = []
users.append(("olivier", 30))
users.append(("jean-louis", 90))
cursor.executemany("""
INSERT INTO users(name, age) VALUES(?, ?)""", users)
conn.commit()

cursor.execute("""SELECT id, name, age FROM users""")
user1 = cursor.fetchone()
print(user1)

cursor.execute("""SELECT id, name, age FROM users""")
rows = cursor.fetchall()
for row in rows:
	print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))

id1 = 2
cursor.execute("""SELECT id, name FROM users WHERE id=?""", (id1, ))
response = cursor.fetchone()
print(response)
cursor.execute("""UPDATE users SET age = ? WHERE id = 2""", (31, ))
conn.commit()
cursor.execute("""SELECT id, name FROM users WHERE id=?""", (id1, ))
response = cursor.fetchone()
print(response)

conn.rollback()
id = 2
cursor.execute("""SELECT id, name FROM users WHERE id=?""", (id,))
response = cursor.fetchone()

cursor = conn.cursor()
cursor.execute("""DROP TABLE users""")
conn.commit()

conn.close()

