import csv
import sys

action = sys.argv[1]


if action == "add":
    name = sys.argv[2]
    capacity = sys.argv[3]

    def write_class_csv(name = None, capacity = 30):
        with open('src/classroom.csv','a',newline='') as csvfile:
          class_writer = csv.writer(csvfile, delimiter=',')
          class_writer.writerow([name,capacity])

    write_class_csv(name,capacity)
    sys.stdout.flush()


elif action == "remove":
    name = sys.argv[2]
    f = open("src/classroom.csv")
    r = csv.reader(f)
    row0 = next(r)

    all=[]
    all.append(row0)
    for item in r:
        if item[0]==name:
            pass
        else:
            all.append(item)
    f.close()

    myFile = open('src/classroom.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(all)
