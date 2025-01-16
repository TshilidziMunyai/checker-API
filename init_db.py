# SQLite database and populate it with sample data
# This will generate the products.db file in the root directory.

import sqlite3

conn = sqlite3.connect('products.db')

# Create products table
conn.execute('''CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    availability INTEGER NOT NULL
)''')

# Insert sample data
products = [
    (1, 'Product A', 25.00, 1),
    (2, 'Product B', 50.00, 0),
    (3, 'Product C', 75.00, 1)
]

conn.executemany('INSERT INTO products (id, name, price, availability) VALUES (?, ?, ?, ?)', products)
conn.commit()
conn.close()

print("Database initialized with sample data.")
