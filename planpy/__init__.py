

from dateutil import parser
import os
from structures import construction, it
from tasks import TaskRegister


#https://mermaid-js.github.io/mermaid/#/gantt


class Resource(Tools):
    """
    Main resource class
    """
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate



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






class Project(Tools):

    """
    Main project class of library.

        Initialise a new project:
            Methods can then be added off the project and visualised.

    """
    projects = []

    def __init__(self,project_name, project_type="it"):

        self.project_name = project_name
        self.__class__.projects.append(self)
        self.project_type = project_type
        self.task_register = TaskRegister(project_name + ': task register')


    def __str__(self):

        for instance in self.projects:
            return instance.name


    def create_directory(self, os_dir):

            os.chdir(os_dir)
            os.mkdir(self.project_name)
            os.chdir(os_dir+"/"+self.project_name)

            if self.project_type == "construction":

                for folder in construction.construction:

                    os.mkdir(folder)
            else:

                for folder in it.it:

                    os.mkdir(folder)


    def add_task(task_name):

        self.task_regiser







class Budget:
    """

    Main budget class

    """

    def __init__(self, project, total):
        self.project = project
        self.total = total


    def add_expense():
        pass

    def add_gst():
        pass

    def quarterly_projection():
        pass

    def monthly_projection():
        pass

    def cost_category():
        pass


class Reporting:
    """
     Main reporting class
    """

    def __init__(self, project):
        self.project = project


    def month_summary():
        pass

    def key_risks():
        pass

    def key_person_dependencies():
        pass

    def overdue_tasks():
        pass

    def overdue_risks():
        pass
