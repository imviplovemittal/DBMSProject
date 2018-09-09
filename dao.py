import sqlite3

conn = sqlite3.connect('databse.db')
print("Database Opened")


def give_login():
    return conn.execute("SELECT cust_id,password from Customers")


def get_vehicles():
    return conn.execute("select type,price_km,no_of_passengers from vehicles where left>0")

# conn.close()
