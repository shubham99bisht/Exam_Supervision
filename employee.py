import csv


"""
name = "shubham"
pos = "teacher"
dept = "IT"
"""

def write_emp_csv(name = None,pos = None,dept = None):
    with open('employee.csv','a',newline='') as csvfile:
      emp_writer = csv.writer(csvfile, delimiter=',')
      emp_writer.writerow([name,pos,dept])


#write_emp_csv('shubham',dept='comps')
