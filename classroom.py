import csv

def write_class_csv(name = None, capacity = 30):
    with open('classroom.csv','a',newline='') as csvfile:
      class_writer = csv.writer(csvfile, delimiter=',')
      class_writer.writerow([name,capacity])


#write_class_csv('C201',50)
