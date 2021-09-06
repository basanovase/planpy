

from dateutil import parser
from os import chdir

class Tools:


    """

    Main function class

    """

    def add_start_date(self, start_date):

        """

        Format: '2019-12-04'

        """
        try:
            start_date = parser.parse(start_date)
            self.start_date = start_date

            return self.start_date
        except Exception as E:

            print(str(E))




    def add_end_date(self, end_date):
        if self.start_date:

            try:

                end_date = parser.parse(end_date)
                self.end_date = end_date
                return self.end_date

            except Exception as E:

                print(str(E))

        else:

            raise ValueError('You must add a start date prior to an end date.')


    def add_budget(self, budget):
        try:

            budget = int(budget)
            self.budget = budget
            return self.add_budget

        except:
            print(str(E))



    def assigned_to(self, assigned):
        self.assigned = assigned
        return self.assigned

    def business_owner(self, business_owner):
        self.business_owner = business_owner
        return self.business_owner


class Risk(Tools):
    """
    Main risk class of library.

    """
    risks = []

    def __init__(self, name, project, progress):
        self.name = name
        self.project = project
        self.progress = progress
        self.__class__.risks.append(self)



class Task(Tools):
    """Main task class of library.

            Inititlise a new project:
                Methods can then be added off task

    """
    tasks = []

    def __init__(self, name, project, progress):
        self.name = name
        self.project = project
        self.progress = progress
        self.__class__.tasks.append(self)



class Project(Tools):

    """
    Main project class of library.

        Initialise a new project:
            Methods can then be added off the project and visualised.

    """
    projects = []

    def __init__(self,project_name):
        self.project_name = project_name
        self.__class__.projects.append(self)


    def __str__(self):
        for instance in self.projects:
            return instance.name

    def start(self, os_dir):
        os.chdir(os_dir)





class Reporting:

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
