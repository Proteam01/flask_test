import sqlite3
conn = sqlite3.connect('flask.db')
sql = 'create table books(id integer primary key,name varchar(40), type varchar(40) )'
conn.execute(sql)
conn.execute("insert into books (name,type) values('forest gump','drama') ")
conn.execute("insert into books (name,type) values('the count of monte cristo','drama') ")
conn.execute("insert into books (name,type) values('dracula','terror') ")
conn.execute("insert into books (name,type) values('F#','education') ")
conn.commit()
conn.close()