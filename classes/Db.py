from cmath import nan
from re import L
import mysql.connector
import pandas as pd

'''
This class allows to connect to the database, to close connections and to execute queries
'''
class TwDb:

    # Initial params
    def __init__(self, host, user, passwd, database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

        self.connection = None
        self.cursor = None
    
    # Connection
    def conn(self):

        if (self.connection == None):    
            try:
                self.connection = mysql.connector.connect(
                    host = self.host,
                    user = self.user,
                    passwd = self.passwd,
                    database = self.database,
                    auth_plugin='mysql_native_password',
                    consume_results=True)
                print('Connection stablished.')               
            except mysql.connector.Error as err:
                print(err)
        else:
            print('Connection already exists.')

    # Disconnection
    def disconn(self):
        
        if (self.connection == None):
            print('There is no connection.')
        else:
            try:
                self.connection.close()
                self.cursor.close()
                self.connection = None
                print('Connection closed.')
            except mysql.connector.Error as err:
                print(err)
    
    # Execute query
    def executeQuery(self, query):
        if (self.connection == None):
            print('There is no connection.')
        else:
            try:
                if (self.cursor == None):
                    self.cursor = self.connection.cursor()
                self.cursor.execute(query) 
                data = [i for i in self.cursor.fetchall()] # list with rows
                columns = [i for i in self.cursor.column_names] # list with column names
                self.connection.commit()

                if (len(data) > 0):
                    print('Query successfully executed.')
                    return pd.DataFrame(data=data, columns=columns) # return the dataframe
                else:
                    print('Query successfully executed.')
                
            except mysql.connector.Error as err:
                print(err)
    
    # Fill a table
    def fillTable(self, df, table_name):
        if(self.connection == None):
            print('There is no connection.')
        else:
            try:
                # Generate a string with column names separated by comma and another one with %s
                col_str = ''
                var_str = ''
                for col in df.columns:
                    col_str = col_str+col+','
                    var_str = var_str+'%s,'
                col_str = col_str[:-1]
                var_str = var_str[:-1]
                
                # 
                sql = "INSERT INTO "+table_name+"("+col_str+") VALUES("+var_str+");"
                for row in df.values.tolist():
                    self.cursor.execute(sql, tuple(row))
                self.connection.commit()

                print('The table '+table_name+' has been filled.')
            
            except mysql.connector.Error as err:
                print(err)
                self.connection.rollback()

                        
                