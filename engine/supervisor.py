import csv
import sys

action = sys.argv[1]


if action == "add":
    name = sys.argv[2]
    dept = sys.argv[3]
    pos = sys.argv[4]

    def write_emp_csv(name = None,pos = None,dept = None):
        with open('src/supervisor.csv','a',newline='') as csvfile:
          emp_writer = csv.writer(csvfile, delimiter=',')
          emp_writer.writerow([name,pos,dept])

    write_emp_csv(name,dept,pos)
    sys.stdout.flush()


elif action == "remove":
    name = sys.argv[2]
    dept = sys.argv[3]
    pos = sys.argv[4]
    f = open("src/supervisor.csv")
    r = csv.reader(f)
    row0 = next(r)
    flag = 0
    all=[]
    all.append(row0)
    for item in r:
        if item[0]==name and item[1]==dept and item[2]==pos:
            pass
        else:
            all.append(item)
    f.close()

    myFile = open('src/supervisor.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(all)
