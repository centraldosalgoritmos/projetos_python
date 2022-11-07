# -*- coding: utf-8 -*-
from configparser import ConfigParser
from typing import List

import psycopg2
import os

from psycopg2 import extras



class DatabaseManager:

    __connection = None


    def get_connection():
        if not DatabaseManager.__connection or DatabaseManager.__connection.closed:
            DatabaseManager.__connection = psycopg2.connect(database = 'db_biblioteca', user = 'postgres', password = '12345678', host = 'localhost')
            DatabaseManager.__connection.autocommit = True
        return DatabaseManager.__connection


    def close_connection():
        if DatabaseManager.__connection and not DatabaseManager.__connection.closed:
            DatabaseManager.__connection.close()
        DatabaseManager.__connection = None


