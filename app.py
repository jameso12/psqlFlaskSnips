from distutils import command
from sqlalchemy import create_engine
# This is where my database's URI was, you do not need to import this
from notes import MY_DB_STRING
DB_STRING_FORMAT = "dbengine://user/password@connection:port/database_name"
# place holder
DB_STRING = MY_DB_STRING
# Connecting to the db
db = create_engine(DB_STRING)
# You need to install the extension if it does not exist in
#  order to use the uuid like I did in this snip.
installExtensionCMD = 'CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'
# Command to ccreate table
createTableCMD = "CREATE TABLE IF NOT EXISTS created (id uuid PRIMARY KEY DEFAULT uuid_generate_v4(), name VARCHAR(40) NOT NULL)"
# Inserting into table
insertToTable = "INSERT INTO created(name) VALUES ('Someone')"
# Updating row
updatingRow = "UPDATE created SET name='changed' WHERE name='Someone'"
# Deleting row
deletingRow = "DELETE FROM created WHERE name='changed'"
# Execute commands
db.execute(installExtensionCMD)
db.execute(createTableCMD)
db.execute(insertToTable)
db.execute(updatingRow)
db.execute(deletingRow)