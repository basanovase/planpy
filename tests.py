import planpy



new_project = planpy.project("rest")


new_project.add_start_date('2019-12-04')


print(new_project.start_date)

another_project = planpy.project('test').add_start_date('2021-01-20')

another_project = planpy.project('test').add_end_date('2020-01-20')
