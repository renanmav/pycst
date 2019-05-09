import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)

sys.path.insert(0, parentdir)

from src.pycst.com.server import create_server, get_method  # noqa: E402

cst = create_server()

mws = get_method(cst, 'NewMWS')

assert str(type(mws)) == "<class 'method'>"
