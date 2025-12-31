"""
This module receives data from the AppMonitors and stores it
in the database.
"""

from pathlib import Path
from datetime import datetime
from app.db.database import Database

class DBHandler:
    def __init__(self):
        self.db = Database()

    def register_focus_loss(self):
        query = '''
                INSERT INTO focus_loss (reg_time, reg_date)
                VALUES (time(), date());
            '''
            
        try:
            self.db.cursor.execute(query)
            self.db.conn.commit()
        except Exception as e:
            log_path = str(Path(__file__).resolve().parent) + '_errors.log'
            reg_time = datetime.now().strftime("%H:%M:%S")
            reg_date = datetime.now().strftime("%d/%m/%Y")
            with open(log_path, "a") as f:
                msg = f'[{reg_date} - {reg_time}] Exception {e}\n'
                f.write(msg)