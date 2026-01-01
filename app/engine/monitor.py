from time import time, sleep
from threading import Lock
from .db_handler import DBHandler

class Monitor:
    def __init__(self):
        """
        General AppMonitor initialization
        Args:
            db: Database object for storing monitor data
        """
        self.db = DBHandler()
        self.focus_tolerance: int = None
        self.original_app_name: str = None
        self.current_app_name: str = None
        self.verification_lock = Lock()
        self.activity_start = int(time())
        self.new_activity_start = None
        self.activity_id: int = None

    def focus_change(self):
        """
        Perform the focus switching between activities
        Only one verification runs at a time. Focus changes during verification are ignored.
        A focus change is only considered valid if the user stays in the new app
        for more than the focus_tolerance period.
        """
        if not self.verification_lock.acquire(blocking=False):
            print("[DEBUG] Focus change skipped: verification already running")
            return
                
        # Check if the newly focused app is from the same activity
        if self.activity_id == self.db.get_activity_id(self.current_app_name):
            print("[DEBUG] Focus change skipped: new app associated with the same activity")
            self.verification_lock.release()
            return

        try:
            timestamp: float = time()
            # Wait for the focus_tolerance period
            sleep(self.focus_tolerance)

            # Check if the user returned to the original app
            if self.original_app_name == self.current_app_name:
                print("[DEBUG] Focus change aborted: user returned to original app")
                return

            # Compute the focus change
            duration = int(timestamp - self.activity_start)
            print("[DEBUG] Focus changed")
            print(f"Previous app: {self.original_app_name}")
            print(f"Current app: {self.current_app_name}")
            print(f"[DEBUG] Duration: {duration} seconds")
            self.original_app_name = self.current_app_name
            
            # Send data to the logger
            # -- Register focus period
            self.db.register_focus(self.activity_id, duration)
            # -- Register focus loss
            self.db.register_focus_loss()

            # Update the new activity on the monitor's side
            self.activity_id = self.db.get_activity_id(self.current_app_name)

        finally:
            self.activity_start = self.new_activity_start   # Start monitoring the new activity
            self.verification_lock.release()

    def run(self):
        """
        Placeholder for the run method.
        Platform-specific monitors should override this method.
        """
        raise NotImplementedError("The run method must be implemented by the platform-specific monitor.")