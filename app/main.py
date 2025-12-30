from app.engine.interface import AppMonitor
from app.db.database import Database

if __name__ == "__main__":
    # Initialize the database
    db = Database()
    
    # Launch the AppMonitor with database
    monitor = AppMonitor.alloc().init()
    monitor.set_database(db)
    monitor.run()