from tools import Tool


class Resource(Tool):
    """
    Main resource class
    """
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate
