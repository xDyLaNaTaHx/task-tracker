from datetime import datetime

def get_current_timestamp():
    """
    Return current timestamp as an ISO-like string.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")