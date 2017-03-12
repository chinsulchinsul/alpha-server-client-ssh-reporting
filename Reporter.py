#!/usr/bin/env python
import mysql.connector
import sys
import Server




def main():
    db_user = 'root'
    db_password = 'strong_password'
    db_name = 'ssh_access_reports'
    db_host = '127.0.0.1'
    db_table = 'report'


    print "Connecting to mysql."
    connection = Server.initiate_db_connection(db_user,db_password,db_host)

    print "Getting data from database"
    query = 'SELECT * FROM %s.%s' %(db_name,db_table)
    response = Server.db_execute(connection,query,True)
    print response




if __name__ == "__main__":
    main()