from sqlite3 import connect
from sqlalchemy import create_engine
from notes import MY_DB_STRING
DB_STRING_FORMAT = "dbengine://user/password@connection:port/database_name"
# Place hoder
DB_STRING = MY_DB_STRING

# The idea behind this class is encapsulation and a certain leve of abstraction
class DB:
    # Again making sure that the eextension is downloaded
    installExtensionCMD = 'CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'
    # I don't even know if i am going to use this lol    
    rowNOtFound = "-1"
    # Constructor to avoid doing everything manually
    def __init__(self):
        """This function creates the connection to the database and installs the necessary extension to it."""
        # Create connection
        self.connectDB()
        # Install extension
        self.db.execute(self.installExtensionCMD)
        # TODO Create the users table
        self.db.execute("DROP TABLE IF EXISTS users")
        self.db.execute("""CREATE TABLE users (
id uuid PRIMARY KEY DEFAULT uuid_generate_v4 (),
username VARCHAR(20) UNIQUE NOT NULL,
password VARCHAR(20) NOT NULL
)""")

    def connectDB(self):
        self.db = create_engine(DB_STRING)
    # Functions with commun table interactions
    def createRow(self,*, table, columns, values):
        """This function will add a row to a table."""
        return self.db.execute(f"INSERT INTO {table}({columns}) VALUES ({values})")
    
    def getRow(self,*,table, columns, conditions):
        """This function returns rows that meet a condition"""
        return self.db.execute(f"SELECT {columns} FROM {table} WHERE {conditions}")
    
    def updateRow(self,*,table, columnsWithNewValues, conditions):
        """THis function updates rows that meet a condition"""
        return self.db.execute(f"UPDATE {table} SET {columnsWithNewValues} WHERE {conditions}")
    
    def deleteRow(self,*, table, conditions):
        """This function deletes rows that meet a conditrion""" 
        return self.db.execute(f"DELETE FROM {table} WHERE {conditions}")

# experimenting:
# myDB = DB()
# myDB.createRow(table='users', columns="username, password", values="'james', '1234'")
# myDB.createRow(table='users', columns="username, password", values="'jams', '1232'")
# for r in myDB.getRow(columns="username, password",conditions="1=1", table="users" ):  
#     print(r[0]) # aparently this is a tuple, or at least an indexed iterable

myDB = create_engine(MY_DB_STRING)
print(myDB.execute("select password from om;").fetchone()) 
# fetch all create an array of tuples
# fetchone gets a tuple
# if fetchall has fails condition empty array
# if fetcone fails condition None

    