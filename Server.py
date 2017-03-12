#!/usr/bin/env python
import mysql.connector

def initiate_db_connection(user_name, password, host_name):
    try:
        cnx = mysql.connector.connect(user=user_name,
                                    password=password,
                                    host=host_name)
        print "MySQL connection succeeded.\n"
        return cnx
    except mysql.connector.Error as err:
        print "MySQL connection error %s" %str(err)
    


def close_db_connection(cnx):
    try:
        cnx.close()
        print "Database connection closed successfully.\n"
    except mysql.connector.Error as err:
        print "Error closing db connection %s" %str(err)
        exit(1)

def db_execute(cnx,sql):
    try:
        cursor = cnx.cursor()
        cursor.execute(sql)
        print "Query executed successfully.\n"
    except mysql.connector.Error as err:
        print "Error executing query %s" %str(err)
        exit(1)

def main():
    db_user = 'root'
    db_password = 'strong_password'
    db_name = 'ssh_access_reports'
    db_host = '127.0.0.1'
    db_table = 'report'

    print "Connecting to mysql."
    connection = initiate_db_connection(db_user,db_password,db_host)

    print "Creating databse if not existing."
    query = 'CREATE DATABASE IF NOT EXISTS %s' %db_name
    db_execute(connection,query)

    print "Creating table if not existing."
    query = 'CREATE TABLE IF NOT EXISTS %s.%s ( ID int, NodeName varchar(255), AttemptCount int );' %(db_name,db_table)
    db_execute(connection,query)

    print "Closing database connection."
    close_db_connection(connection)

if __name__ == "__main__":
    main()
