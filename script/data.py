import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="chatgpt",
    database="chatgpt"
)
#Print if successful
print(mydb)

# Create a cursor
mycursor = mydb.cursor()

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