import win32com

""" in case I want to run directly this script

import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)

sys.path.insert(0, parentdir)

from src.pycst.com.server import create_server  # noqa: E402
"""

from pycst.com.server import create_server

cst = create_server()

assert type(cst) == win32com.client.CDispatch
