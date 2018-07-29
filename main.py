import employee
import classroom
import dates

c="ys "
while c == "Y" or c =="y":
    name,pos,dept = input("Enter employee details: space separated").split()

    print(name+"\n"+pos,"\n"+dept)
    employee.write_emp_csv(name,pos,dept)
    c = input("continue: Y|N")


c="y"
while c == "Y" or c =="y":
    name = input("Enter classroom details")
    print(name)
    classroom.write_class_csv(name)
    c = input("continue: Y|N")


c="y"
while c == "Y" or c =="y":
    li = list(map(str,input("Enter exam dates details").split()))
    dates.write_dates_csv(li)
    c = input("continue: Y|N")
