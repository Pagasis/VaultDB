from pickle import dump

import mysql.connector as connector


def fetch_password_for_sql():
    password=input('Enter MySQL Password')
    with open('root.key', 'wb') as file:
        dump(password,file)
    return(password)

def create_database_and_password():
    print("Looking for MSQL Installation ....")
    passwords=fetch_password_for_sql()
    print("Attempting to Connect")
    connection = connector.connect(host="localhost", user="root", password=passwords)

    # Defining cursor
    cursor = connection.cursor()
    with open("data.sql",) as file:
        for line in file:
            try:
                cursor.execute(line[:-1])
            except:
                pass
    connection.commit()
    cursor.close()
    connection.close()


