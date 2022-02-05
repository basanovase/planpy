



class Task:

    """

    Main task class


    """
    def __init__(self, name, project, progress, fte):
            self.name = name
            self.project = project
            self.progress = progress
            self.__class__.tasks.append(self)
            self.fte = fte
            self.activetasks = []






class TaskRegister(Tool):
    """

    Main task class of library.

            Inititlise a new project:
                Methods can then be added off task

    """
    tasks = []

    def __init__(self):

        self.activetasks = []

    def progress(self, percentage_complete):

        self.progress = percentage_complete

        return self.progress

    def add_task(self, task_name):

        self.activetasks.append(task_name)
