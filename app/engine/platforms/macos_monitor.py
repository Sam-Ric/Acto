"""
macOS AppMonitor implementation.
Uses the AppKit APIs and the PyObjC bridge to identify changes in the
user's focus.
"""

from AppKit import NSWorkspace, NSObject
from objc import super as objc_super
from app.engine.utils import load_config
from PyObjCTools import AppHelper
from threading import Thread, Lock
from time import time
from app.engine.monitor import Monitor

class MacOSAppMonitor(NSObject, Monitor):
    def init(self):
        """
        App Monitor initialization
        """
        config = load_config()
        self = objc_super(MacOSAppMonitor, self).init()
        if self is None:
            return None

        # Python-specific initialization
        self.focus_tolerance = config['engine']['focus_tolerance']
        self.verification_lock = Lock()
        self.current_app_name = None
        self.activity_start = int(time())
        
        workspace = NSWorkspace.sharedWorkspace()
        self.original_app_name = workspace.activeApplication()['NSApplicationName']
        notification_center = workspace.notificationCenter()
        notification_center.addObserver_selector_name_object_(
            self,
            "appActivated:",
            "NSWorkspaceDidActivateApplicationNotification",
            None,
        )
        print(f"Initial active app: {self.original_app_name}")
        return self

    def appActivated_(self, notification):
        """
        Method called when the active application changes
        """
        app = notification.userInfo().get("NSWorkspaceApplicationKey")
        if app:
            self.current_app_name = app.localizedName()
            print(f"Switched to: {self.current_app_name}")
            # Only start a new verification if one is not already running
            if not self.verification_lock.locked():
                Thread(name="focus_thread", target=self.focus_change).start()
            else:
                print("[DEBUG] Focus change ignored: verification in progress")
        else:
            print("No app info in notification")

    def run(self):
        """
        Start the macOS event loop.
        """
        print("Monitoring active applications. Press ^C to exit.")
        try:
            AppHelper.runConsoleEventLoop()  # Run the macOS event loop
        except KeyboardInterrupt:
            print("Exiting...")