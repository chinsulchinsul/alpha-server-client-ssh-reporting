#!/usr/bin/env python
import mysql.connector

def initiate_db_connection(user_name, password, host_name):
    try:
        cnx = mysql.connector.connect(user=user_name,
                                    password=password,
                                    host=host_name)
        print "MySQL connection succeeded"
        return cnx
    except mysql.connector.Error as err:
        print "MySQL connection error %s" %str(err)
    


def close_db_connection(cnx):
    try:
        cnx.close()
        print "Database connection closed successfully."
    except mysql.connector.Error as err:
        print "Error closing db connection %s" %str(err)

def db_execute(cnx,sql):
    try:
        cursor = cnx.cursor()
        cursor.execute(sql)
        print "Query executed successfully."
    except mysql.connector.Error as err:
        print "Error executing query %s" %str(err)

def main():
    db_user = 'root'
    db_password = 'strong_password'
    db_name = 'ssh_access_reports'
    db_host = '127.0.0.1'

    print "Connecting to mysql"
    connection = initiate_db_connection(db_user,db_password,db_host)

    print "Creating databse if not existing"
    create_db_query='CREATE DATABASE IF NOT EXISTS %s' %db_name

    db_execute(connection,create_db_query)

    print "Closing database connection"
    close_db_connection(connection)

if __name__ == "__main__":
    main()
