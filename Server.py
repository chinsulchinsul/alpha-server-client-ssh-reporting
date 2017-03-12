import mysql.connector

def initiate_db_connection(user_name, password, databes_name, host_name):
	try:
  		cnx = mysql.connector.connect(user=user_name,
                                	database=database,
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
		Print "Error closing db connection %s" %str(err)
