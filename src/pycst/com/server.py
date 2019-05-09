from win32com import client


def create_server(application_name='CSTStudio.application'):
    """
    Initialize the CST application

    Parameters:
    ----------
    application_name : string that references CST Studio Suite

    Returns:
    ----------
    cst : win32com.client.CDispatch
        COM Object
    """
    return client.Dispatch(application_name)
