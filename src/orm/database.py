from peewee import MySQLDatabase
import os

instance = MySQLDatabase(None)

name = os.getenv('DB_NAME')

config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASS'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 3306))
}
