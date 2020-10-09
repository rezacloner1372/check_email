import mysql.connector
from mysql.connector import errorcode
import re
print('connecting to db')
try:
  mydb = mysql.connector.connect(
    user="kilid",
    password='123',
    host="127.0.0.1",
    database="db1"
)
  print('connected to db')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
mycursor = mydb.cursor()

def askemail():
    email = input('plz enter your email: ')
    EMAIL_REGEX = re.compile(r"^[A-Za-z0-9]+@[a-zA-Z]+\.[a-zA-Z]+$")
    if EMAIL_REGEX.match(email):
        print('OK')
    else:
        print('WRONG')
askemail()