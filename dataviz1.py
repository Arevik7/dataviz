import sqlite3
import numpy as np
import time
## sql
connection = sqlite3.connect('data_db.db')
c = connection.cursor()
# creating tables
c.execute("DROP TABLE IF EXISTS values_")
c.execute("DROP TABLE IF EXISTS averages")

c.execute("CREATE TABLE values_ (Id int, value int)")
c.execute("CREATE TABLE averages (Id int, value real)")

i = 0
j = 0
a = 0

while True:
	b = 0
	for counter in range(0,7):
		i += 1
		a = np.random.randint(1,6)
		b += a
		c.execute("INSERT INTO values_ values ({},{})".format(i,a))
		#connection.commit()
	j += 1
	b = b / 7
	c.execute("INSERT INTO averages values ({},{})".format(j,b))
	connection.commit()

	time.sleep(0.5)

