from app.engine.interface import AppMonitor
from app.engine.utils import load_config

if __name__ == "__main__":
    # Instantiate the platform-specific AppMonitor
    monitor = AppMonitor()
    monitor.run()