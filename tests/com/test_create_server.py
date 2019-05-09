import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)

sys.path.insert(0, parentdir)

from src.pycst.com.server import create_server, list_methods  # noqa: E402

cst = create_server()

methods = ['Active3D', 'ActiveDS', 'CLSID', 'CloseProject', 'FileNew', 'NewCS', 'NewDS', 'NewDesign', 'NewEMS',
           'NewMPS', 'NewMWS', 'NewPCBS', 'NewPS', 'OpenDesign', 'OpenFile', 'Quit', 'ReleaseUniqueID', 'coclass_clsid']

assert list_methods(cst) == methods
