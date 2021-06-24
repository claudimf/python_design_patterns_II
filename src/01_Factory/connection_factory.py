# -*- coding: utf-8 -*-
import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
                            host=os.getenv('MYSQL_HOST'),
                            user=os.getenv('MYSQL_USER'),
                            password=os.getenv('MYSQL_ROOT_PASSWORD'),
                            db=os.getenv('MYSQL_DATABASE')
                            )
