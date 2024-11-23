import mysql.connector
import threading

class MySQL:
    LOCK = threading.Lock()
    TABLES = {}
    conn = None

    @staticmethod
    def init(host, port, user, password, database):
        MySQL.host = host
        MySQL.port = port
        MySQL.user = user
        MySQL.password = password
        MySQL.database = database
        MySQL._connect()

    @staticmethod
    def _connect():
        """Establish a connection to the database."""
        MySQL.conn = mysql.connector.connect(
            host=MySQL.host,
            port=MySQL.port,
            user=MySQL.user,
            password=MySQL.password,
            database=MySQL.database
        )

    @staticmethod
    def _ensure_connection():
        """Ensure the connection is active or reconnect if needed."""
        if MySQL.conn is None or not MySQL.conn.is_connected():
            try:
                MySQL._connect()
            except Exception as e:
                raise RuntimeError(f"Failed to reconnect to the database: {e}")

    @staticmethod
    def commit():
        MySQL._ensure_connection()
        MySQL.conn.commit()

    @staticmethod
    def cursor():
        MySQL._ensure_connection()
        return MySQL.conn.cursor(dictionary=True)

    @staticmethod
    def fetch_one(query, args=()):
        with MySQL.LOCK:
            cursor = MySQL.cursor()
            cursor.execute(query, args)
            data = cursor.fetchone()
            cursor.close()
            return data

    @staticmethod
    def fetch_all(query, args=()):
        with MySQL.LOCK:
            cursor = MySQL.cursor()
            cursor.execute(query, args)
            data = cursor.fetchall()
            cursor.close()
            return data

    @staticmethod
    def insert_into(table, columns, values):
        with MySQL.LOCK:
            cursor = MySQL.cursor()
            cursor.execute(
                f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join('%s' for _ in range(len(values)))})",
                values
            )
            MySQL.commit()
            row_id = cursor.lastrowid
            cursor.close()
            return row_id

    @staticmethod
    def update(table, columns, condition, args):
        with MySQL.LOCK:
            cursor = MySQL.cursor()
            cursor.execute(
                f"UPDATE {table} SET {', '.join([f'{column} = %s' for column in columns])} WHERE {condition}",
                args
            )
            MySQL.commit()
            cursor.close()

    @staticmethod
    def delete(table, condition, args):
        with MySQL.LOCK:
            cursor = MySQL.cursor()
            cursor.execute(
                f"DELETE FROM {table} WHERE {condition}",
                args
            )
            MySQL.commit()
            cursor.close()
