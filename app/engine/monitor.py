import sys
from time import time, sleep
from threading import Lock

class Monitor:
    def __init__(self, db=None):
        """
        General AppMonitor initialization
        Args:
            db: Database object for storing monitor data
        """
        self.db = db
        self.focus_tolerance = None
        self.original_app_name = None
        self.current_app_name = None
        self.verification_lock = Lock()
        self.activity_start = int(time())

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
        try:
            timestamp = time()
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
            # TODO -> Send data to the logger
        finally:
            self.verification_lock.release()

    def run(self):
        """
        Placeholder for the run method.
        Platform-specific monitors should override this method.
        """
        raise NotImplementedError("The run method must be implemented by the platform-specific monitor.")