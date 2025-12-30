"""
Database module for Acto application.
Handles SQLite database connections and operations.
"""

import sqlite3
import os

class Database:
    def __init__(self, db_path=None):
        """
        Initialize database connection.
        Args:
            db_path: Path to the SQLite database file. If None, uses default location.
        """
        if db_path is None:
            db_path = os.path.dirname(__file__) + "/database.db"
        
        # Connect to the database
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
    
        # Set up the database schema if it wasn't setup
        if db_path != ":memory:":
            db_size = os.path.getsize(db_path)
        else:
            db_size = 0

        if db_size == 0:
            schema_path = os.path.dirname(__file__) + "/schema.sql"
            with open(schema_path, "r") as f:
                schema = f.read()
                schema = schema.split(";")
            for query in schema:
                self.cursor.execute(query)
    
    def close(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()
