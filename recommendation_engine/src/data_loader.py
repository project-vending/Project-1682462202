python
import pandas as pd
import numpy as np
import psycopg2

class Recommender:
    def __init__(self, dbname, host, port, user, password):
        self.dbname = dbname
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.conn = self.create_connection()

    def create_connection(self):
        conn = psycopg2.connect(
            dbname=self.dbname,
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
        )
        return conn

    def get_recommendations(self, user_id, n=5):
        sql = '''
            SELECT *
            FROM recommendations
            WHERE user_id = %s
            ORDER BY score DESC
            LIMIT %s;
        '''
        cursor = self.conn.cursor()
        cursor.execute(sql, (user_id, n))
        results = cursor.fetchall()
        cursor.close()
        return results
