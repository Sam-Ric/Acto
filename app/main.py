from app.engine.interface import AppMonitor
from app.db.database import Database

if __name__ == "__main__":
    # Launch the AppMonitor
    monitor = AppMonitor()
    monitor.run()