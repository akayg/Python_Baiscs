import sqlite3  # Import the SQLite library to interact with SQLite databases.

# Establish a connection to the SQLite database file "student.db".
# If the file does not exist, it will be created.
conn = sqlite3.connect("student.db")

# Create a cursor object to execute SQL commands.
cursor = conn.cursor()

# Create a table named 'users' if it does not already exist.
# The table has three columns: 'id' (integer), 'name' (text), and 'grade' (text).
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, grade TEXT)")

# Insert initial row into the 'users' table.
cursor.execute("INSERT INTO users VALUES(1, 'Abhishek', 'A')")

# Insert 2 more students into the 'users' table.
cursor.execute("INSERT INTO users VALUES(2, 'John', 'B')")
cursor.execute("INSERT INTO users VALUES(3, 'Alice', 'C')")

# Commit the transaction to save changes to the database.
conn.commit()

# Retrieve and print all rows from the 'users' table.
cursor.execute("SELECT * FROM users")
print("Initial table:")
print(cursor.fetchall())

# Update the grade of Abhishek to 'A+'.
cursor.execute("UPDATE users SET grade = 'A+' WHERE name = 'Abhishek'")
conn.commit()

# Delete one student (e.g., John).
cursor.execute("DELETE FROM users WHERE name = 'John'")
conn.commit()

# Retrieve and print the final table.
cursor.execute("SELECT * FROM users")
print("Final table:")
print(cursor.fetchall())

# Close the connection to the database.
conn.close()