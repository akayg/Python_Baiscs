import sqlite3  # Import the SQLite library to interact with SQLite databases.

# Establish a connection to the SQLite database file "mydb.db".
# If the file does not exist, it will be created.
conn = sqlite3.connect("mydb.db")

# Create a cursor object to execute SQL commands.
cursor = conn.cursor()

# Create a table named 'users' if it does not already exist.
# The table has two columns: 'id' (integer) and 'name' (text).
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")

# Insert a row into the 'users' table with id=1 and name='Abhishek'.
cursor.execute("INSERT INTO users VALUES(1,'Abhishek')")

# Commit the transaction to save changes to the database.
conn.commit()

# Retrieve all rows from the 'users' table.
cursor.execute("SELECT * FROM users")

# Print the fetched rows to the console.
print(cursor.fetchall())

# Close the connection to the database.
conn.close()