#  psqlFlaskSnips

This repo is meant to be a place where I can learn how to set up a connection to a postgresql database and do the following:
- connect to the database using python, sqalchemy(with psycopg2)
- create a table
- add a row to that table
- modify that row
- delete that row
## Remember
You must use your **OWN** database URI for this to work. I placed a variable which shows you how your URI could look like. If you do
not know how to make your URI, look at the [SQLALCHEMY docs](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/) for more help.
## How I did it
I followed along a [tutorial](https://www.compose.com/articles/using-postgresql-through-sqlalchemy/) that explained how to use sqlalchemy
with postgresql. In this snip I choose to go with the raw commands (I think that what the approach was called) and I had succes at making 
the table. I used variabes instead of string literal just to make it easier to modify and to have all of the commands near the top of
the script(yes, I know there is not much code, but still...).

## General notes
So I succesfully conected and created a table. It was fairly easy. The only problems a ran into at first were:
1. I added semicolon and you can get away with not adding one
2. I forgot to install the [extension](https://www.postgresqltutorial.com/postgresql-uuid/) to use uuid. 
## Other useful links:
- [Using Multiple Tables](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_using_multiple_tables.htm)
- [Creating a table in postgresql](https://www.postgresqltutorial.com/postgresql-create-table/)
