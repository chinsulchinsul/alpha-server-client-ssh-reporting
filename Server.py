#!/usr/bin/env python
import mysql.connector

def initiate_db_connection(user_name, password, database_name, host_name):
    try:
        cnx = mysql.connector.connect(user=user_name,
                                    database=database_name,
                                    password=password,
                                    host=host_name)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return cnx

def close_db_connection(cnx):
    try:
        cnx.close()
    except mysql.connector.Error as err:
        print "Error closing db connection %s" %str(err)

def db_execute(cnx,sql):
    try:
        cursor = cnx.cursor()
        cursor.execute(sql)
    except mysql.connector.Error as err:
        print "Error executing query %s" %str(err)
def main():
    db_user = 'root'
    db_password = 'strong_password'
    db_name = 'ssh_access_reports'
    db_host = '127.0.0.1'

    connection = initiate_db_connection(db_user,db_password,db_name,db_host)

    create_db_query='CREATE DATABASE IF NOT EXISTS %s' %db_name
