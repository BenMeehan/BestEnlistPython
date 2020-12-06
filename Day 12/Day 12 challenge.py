import json
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# READ JSON DATA
with open('./objects.json') as f:
    data = f.read()

# CREATE A POSTGRESQL DATABASE
conn = psycopg2.connect(user="postgres",
                        password="123")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)


cursor = conn.cursor()
sql = 'CREATE DATABASE datatypedb'
cursor.execute(sql)
print("database created")
conn.close()

# CONNECT TO THE DATABASE
conn = psycopg2.connect(database="datatypedb", user="postgres",
                        password="123")
print("connection established")
cursor = conn.cursor()


# CREATE TABLE
sql = '''CREATE TABLE dtype(
    type VARCHAR,
    example VARCHAR
)'''
cursor.execute(sql)
conn.commit()
print("Table created")


# INSERT INTO TABLE
sql = "INSERT INTO dtype(type,example) VALUES(%s,%s)"

parsed_dict = json.loads(data)
print(parsed_dict)
keys = list(parsed_dict.keys())
val = list(parsed_dict.values())

for i in range(len(keys)):
    cursor.execute(sql, (keys[i], val[i],))


conn.commit()
conn.close()
