import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# Insert data into the table
cursor.execute('''
INSERT INTO users (name, age, email)
VALUES (?, ?, ?)
''', ('John Doe', 30, 'john.doe@example.com'))

# Commit the changes
connection.commit()

# Query the data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the connection
connection.close()