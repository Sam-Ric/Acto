import os
import webview

from app.engine.interface import AppMonitor
from app.db.database import Database

UI_PATH = os.path.join(os.path.dirname(__file__), '..', 'ui')



if __name__ == "__main__":
    # Launch the AppMonitor
    monitor = AppMonitor()
    monitor.run()