
from sqlalchemy import *
#1. Création d’une table :
engine = create_engine('sqlite:///college.db', echo=True)

meta = MetaData()
students = Table('students', meta,
	Column('id', Integer, primary_key=True),
	Column('name', String),
	Column('lastname', String), )
	
addresses = Table('addresses', meta,
	Column('id', Integer, primary_key=True),
	Column('st_id', Integer, ForeignKey('students.id')),
	Column('postal_add', String),
	Column('email_add', String))
meta.create_all(engine)
#2. Insertion de données :

ins = students.insert().values(name='Ravi', lastname='Kapoor')
conn = engine.connect()
result = conn.execute(ins)

#3. Insertion de données multiples :

conn.execute(students.insert(),
						[ {'name':'Rajiv', 'lastname' : 'Khanna'},
						  {'name':'Komal','lastname' : 'Bhandari'},
						  {'name':'Abdul','lastname' : 'Sattar'},
						  {'name':'Priya','lastname' : 'Rajhans'},
						])
						
#4. Requête Select :
s = students.select().where(students.c.id > 2)
result = conn.execute(s)
for row in result:
	print(row)
	
#5. Requête Select complexe :

from sqlalchemy import and_
from sqlalchemy.sql import select, text
s = select([text("* from students")]) \
	.where(
			and_(
					text("students.name between :x and :y"),
					text("students.id > :z")
					)
				)
result = conn.execute(s, x='A', y='L', z='2').fetchall()
print(result)

#6. Requête sur des tables multiples :

s = select([students, addresses]).where(students.c.id == addresses.c.st_id)
result = conn.execute(s)
for row in result:
	print (row)
	
#7. Jointures :
from sqlalchemy import join

j = students.join(addresses, students.c.id == addresses.c.st_id)
stmt = select([students]).select_from(j)
result = conn.execute(stmt)
print(result.fetchall())

#8. And / Or :
from sqlalchemy import or_
stmt = select([students]).where(or_(students.c.name=='Ravi', students.c.id <3))
result = conn.execute(stmt)
print(result.fetchall())

# 9. Asc / Desc :
from sqlalchemy import asc
stmt = select([students]).order_by(asc(students.c.name))
result = conn.execute(stmt)
for row in result:
	print (row)
