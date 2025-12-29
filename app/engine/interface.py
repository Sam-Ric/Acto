"""
This module dynamically imports the appropriate AppMonitor implementation
based on the operating system.
"""

import sys

if sys.platform.startswith("win"):
    from .platforms.windows_monitor import WindowsAppMonitor as AppMonitor
elif sys.platform.startswith("darwin"):
    from .platforms.macos_monitor import MacOSAppMonitor as AppMonitor
else:
    from .platforms.linux_monitor import LinuxAppMonitor as AppMonitor