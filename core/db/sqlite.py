import sqlite3
import threading

class Sqlite:
    
    LOCK = threading.Lock()
    
    def init(database):
        Sqlite.conn = sqlite3.connect(database, check_same_thread=False)

    def commit():
        Sqlite.conn.commit()
    
    def cursor():
        Sqlite.conn.cursor()
        return Sqlite.conn.cursor()
        
    def fetch_one(query, args = ()):
        cursor = Sqlite.cursor()
        data = cursor.execute(query, args).fetchone()
        cursor.close()
        return data

    def fetch_all(query, args = ()):
        cursor = Sqlite.cursor()
        data = cursor.execute(query, args).fetchall()
        cursor.close()
        return data
    
    def insert_into(table, columns, values):
        Sqlite.LOCK.acquire()
        cursor = Sqlite.cursor()
        print(f"INSERT INTO {table} ({', '.join(columns)}) VALUES {values}")
        cursor.execute(f"INSERT INTO {table} ({', '.join(columns)}) VALUES {values}")
        Sqlite.commit()
        row_id = cursor.lastrowid
        cursor.close()
        Sqlite.LOCK.release()
        return row_id
    
    def update(table, columns, condition, args):
        Sqlite.LOCK.acquire()
        cursor = Sqlite.cursor()
        print(f"UPDATE {table} SET {', '.join([f'{column} = ?' for column in columns])} WHERE {condition}")
        cursor.execute(f"UPDATE {table} SET {', '.join([f'{column} = ?' for column in columns])} WHERE {condition}", args)
        Sqlite.commit()
        cursor.close()
        Sqlite.LOCK.release()

    def delete(table, condition, args):
        Sqlite.LOCK.acquire()
        cursor = Sqlite.cursor()
        print(f"DELETE FROM {table} WHERE {condition}")
        cursor.execute(f"DELETE FROM {table} WHERE {condition}", args)
        Sqlite.commit()
        cursor.close()
        Sqlite.LOCK.release()