import sqlite3

conn = sqlite3.connect('databse.db', timeout=10)
print("Database Opened")


def give_login():
    return conn.execute("SELECT cust_id,password from Customers")


def get_vehicles():
    return conn.execute("select v_num,type,price_km,no_of_passengers from vehicles where left>0")


def get_drivers():
    return list(conn.execute("SELECT d_id FROM drivers"))


def get_name(c_id):
    return list(conn.execute("SELECT Name FROM Customers WHERE cust_id = ?", (c_id,)))


def get_d_details(d_id):
    return list(conn.execute("SELECT name,contact FROM drivers WHERE d_id = ?", (d_id,)))


def get_trips():
    return list(conn.execute("SELECT trip_id,start_date,distance,driver_id,v_id FROM trip"))


def get_trips_by_vehicle():
    return list(conn.execute("select count(trip_id),sum(distance), v_id from trip group by v_id"))


def get_trips_by_driver():
    return list(conn.execute("select count(trip_id),sum(distance), driver_id from trip group by driver_id"))

# conn.close()
