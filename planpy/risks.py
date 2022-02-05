from tools import Tool

class Risk(Tool):
    """
    Main risk class of library.

    """
    risks = []

    def __init__(self, name, project, progress):
        self.name = name
        self.project = project
        self.progress = progress
        self.__class__.risks.append(self)
