import mysql.connector
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
# Connect to the database
mydb = mysql.connector.connect(
    host=os.getenv('DATABASE_HOST'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    database=os.getenv('DATABASE_NAME')
)
#Print if successful
print(mydb)


# Create a cursor
mycursor = mydb.cursor()

#Create a table named settings if it does not exist with text for guild and ai_key, int for token and auto increment for id, id should last as it is used to identify the record
mycursor.execute("CREATE TABLE IF NOT EXISTS settings (guild TEXT, ai_key TEXT, token INT, id INT AUTO_INCREMENT PRIMARY KEY)")
 



#Inserting a record
def insert_record(guild, ai_key, token):
    sql = "INSERT INTO settings (guild, ai_key, token) VALUES (%s, %s, %s)"
    val = (guild, ai_key, token)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

#Update a record
def update_record(guild, ai_key, token):
    sql = "UPDATE settings SET ai_key = %s, token = %s WHERE guild = %s"
    val = (ai_key, token, guild)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected by ", guild, "")

#Read a record
def read_record(guild):
    sql = "SELECT * FROM settings WHERE guild = %s"
    val = (guild,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult