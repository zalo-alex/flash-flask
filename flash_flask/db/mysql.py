import mysql.connector
import threading

class MySQL:
    
    LOCK = threading.Lock()
    TABLES = {}
    
    def init(host, port, user, password, database):
        MySQL.conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        MySQL.conn.ping(reconnect=True)

    def commit():
        MySQL.conn.commit()
    
    def cursor():
        return MySQL.conn.cursor(dictionary=True)
        
    def fetch_one(query, args = ()):
        MySQL.LOCK.acquire()
        cursor = MySQL.cursor()
        cursor.execute(query, args)
        data = cursor.fetchone()
        cursor.close()
        MySQL.LOCK.release()
        return data

    def fetch_all(query, args = ()):
        MySQL.LOCK.acquire()
        cursor = MySQL.cursor()
        cursor.execute(query, args)
        data = cursor.fetchall()
        cursor.close()
        MySQL.LOCK.release()
        return data
    
    def insert_into(table, columns, values):
        MySQL.LOCK.acquire()
        cursor = MySQL.cursor()
        print(f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join('%s' for _ in range(len(values)))})")
        cursor.execute(f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join('%s' for _ in range(len(values)))})", values)
        MySQL.commit()
        row_id = cursor.lastrowid
        cursor.close()
        MySQL.LOCK.release()
        return row_id
    
    def update(table, columns, condition, args):
        MySQL.LOCK.acquire()
        cursor = MySQL.cursor()
        print(f"UPDATE {table} SET {', '.join([f'{column} = %s' for column in columns])} WHERE {condition}")
        cursor.execute(f"UPDATE {table} SET {', '.join([f'{column} = %s' for column in columns])} WHERE {condition}", args)
        MySQL.commit()
        cursor.close()
        MySQL.LOCK.release()

    def delete(table, condition, args):
        MySQL.LOCK.acquire()
        cursor = MySQL.cursor()
        print(f"DELETE FROM {table} WHERE {condition}")
        cursor.execute(f"DELETE FROM {table} WHERE {condition}", args)
        MySQL.commit()
        cursor.close()
        MySQL.LOCK.release()