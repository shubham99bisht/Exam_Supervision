import csv
import pdf

emp = []
emp_index = 0
exams = []
classroom = []

with open('date.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        exams.append(row)


with open('employee.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        emp.append(row[0])


with open('classroom.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        classroom.append(row[0])

ctr = 0
final_li =[]

for exm in exams:
    temp_li = [exm[0]]
    for classes in exm[1:]:
        temp_li.append([classes,emp[ctr]])
        ctr+=1
        if ctr>=len(emp):
            ctr=0
    final_li.append(temp_li)

print(final_li)
print(type(classroom))
classroom.sort()
pdf_li = []
for x in final_li:
    temp_li = [x[0]]
    x = x[1:]
    x.sort()
    i,j=0,0
    while i < len(x):
        if x[i][0] == classroom[j]:
            temp_li.append(x[i][1])
            i+=1
        else:
            temp_li.append("None")
        j+=1
    pdf_li.append(temp_li)

for i in range(len(pdf_li)):
    print(pdf_li[i])


pdf.make_pdf(pdf_li)
