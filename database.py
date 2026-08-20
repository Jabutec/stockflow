import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "stockflow.db")

def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA foreign_keys = ON;")
    print("Creating tables....")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(
        product_id TEXT PRIMARY KEY,
        product_name TEXT NOT NULL,
        category TEXT NOT NULL,
        price_zar REAL NOT NULL CHECK(price_zar>=0),
        quantity INTEGER NOT NULL CHECK(quantity >= 0),
        reorder_level INTEGER NOT NULL CHECK(reorder_level >= 0),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS customers(
        customer_id TEXT PRIMARY KEY,
        customer_name TEXT NOT NULL,
        phone TEXT,
        email TEXT,
        loyalty_points INTEGER NOT NULL CHECK(loyalty_points>=0),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP 
     )              
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales(
        sale_id TEXT PRIMARY KEY,
        customer_id TEXT NOT NULL,
        sale_total_zar REAL NOT NULL CHECK(sale_total_zar>=0),
        payment_method TEXT CHECK(payment_method IN('cash', 'digital')),
        sale_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sale_items(
        sale_item_id TEXT PRIMARY KEY,
        sale_id TEXT NOT NULL,
        product_id TEXT NOT NULL,
        quantity INTEGER NOT NULL CHECK(quantity > 0),
        unit_price_zar REAL NOT NULL CHECK(unit_price_zar>=0),
        line_total_zar REAL NOT NULL CHECK(line_total_zar>=0),
        FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """)
    
    conn.commit()
    conn.close()
    print(f"Database initialized successfully at {DB_PATH}")
    
if __name__ == "__main__":
    init_database()
                   
    