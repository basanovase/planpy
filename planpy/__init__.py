

from dateutil import parser
import os
#from structures import construction, it
from tasks import TaskRegister
from resource import Resource
from risks import Risk
#https://mermaid-js.github.io/mermaid/#/gantt
from budget import Budget
from reports import Report
from tools import Tool




class Project(Tool):

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
