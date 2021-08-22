import planpy



new_project = planpy.project("rest")


new_project.add_start_date('2019-12-04')
new_project.add_end_date('2020-01-01')

print(new_project.start_date)
