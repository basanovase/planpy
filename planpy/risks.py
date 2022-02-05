
class Risk(Tools):
    """
    Main risk class of library.

    """
    risks = []

    def __init__(self, name: str, project: str, progress: float):
        self.name = name
        self.project = project
        self.progress = progress
        self.__class__.risks.append(self)
