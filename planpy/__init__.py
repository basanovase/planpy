import pandas as pd





class task:
    """Class for tasks"""
    def __init__(self, subject, start_date, completion_date, budget):
        self.subject = subject
        self.start_date = start_date
        self.completion_date = completion_date
        self.budget = budget


class project:

    """
    Main project class of library.

        Initialise a new project:
            Methods can then be added off the project and visualised.

    """

    def __init__(self,project_name, start_date, end_date, budget):
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget


    def add_task():
        
        pass
