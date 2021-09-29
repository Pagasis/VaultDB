# Importing MySQL connector
import mysql.connector as connecter
# Importing date function
from datetime import date

# Connecting to database
connection = connecter.connect(host="localhost",database="vaultdb",user="root",password="")

# Defining cursor
cursor = connection.cursor()

def display_sites():
    # Executing MySQL query to show all stored site names
    cursor.execute("select Website_or_App from vault;")
    data = cursor.fetchall()
    # Displaying all site names
    for records in data:
        print(records)

# Function to display all records
def display(a,app=None):
    try:    
        if a == 'a':
            # Executing MySQL query
            cursor.execute(f"select * from vault;")
            # Fetch all records
            data = cursor.fetchall()
            if data != []:
                for records in data:
                    print(records)
            else:
                print("Seems your vault is empty")
        elif a == 's':
            # Executing MySQL query
            cursor.execute("select * from vault where Website_or_App = '%(app)s';",{'app':app})
            # Display record
            record = cursor.fetchone()
            return record
        else:
            print("Invalid Input!")
    except Exception as e:
        print(f"Error : {e}")

# Function to add pw to database
def add(app, uname, pw):
    # Executing MySQL query
    cursor.execute("insert into vault(Website_or_App,UNAME,PASS,Date_Added) values(%(app)s,%(uname)s,%(pw)s,%(date)s);",{'app':app,'uname':uname,'pw':pw,'date':date.today()})
    # Commiting changes
    connection.commit()
    del app,uname,pw

# Function to remove pw from database
def remove(app):
    # Executing MySQL query
    cursor.execute("delete from vault where Website_or_App = %(app)s;",{'app':app})
    # Commiting changes
    connection.commit()
    del app

# Function to update pw
def update(app,pw):
    # Executing MySQL query
    cursor.execute("update vault set PASS = %(pw)s where Website_or_App = %(app)s;",{'pw':pw,'app':app})
    # Commiting changes
    connection.commit()
    del app,pw
