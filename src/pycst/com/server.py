from win32com.client.gencache import EnsureDispatch


def create_server(application_name='CSTStudio.application'):
    """
    Initialize the CST application

    Parameters:
    ----------
    application_name : string that references CST Studio Suite

    Returns:
    ----------
    cst : win32com.gen_py.cst design environment 1.0 Type Library.IApplication
        COM Object
    """
    return EnsureDispatch(application_name)


def list_methods(interface):
    """
    List all explicit methods of `interface`, hidding methods that starts with '_'

    Parameters:
    ----------
    interface : interface of CST Studio

    Returns:
    ----------
    methods : array of string
        Explict methods of interface
    """
    methods = []

    for key in dir(interface):
        method = str(key)
        if not method.startswith('_'):
            methods.append(method)

    return methods
