import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def make_pdf(pdf_li):

    classroom = []
    with open('src/classroom.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            classroom.append(row[0])
    del(classroom[0])
    classroom.sort()


    fig, ax = plt.subplots()

    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    df = pd.DataFrame(pdf_li, columns=(["Dates"]+classroom))

    ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    fig.tight_layout()

    from matplotlib.backends.backend_pdf import PdfPages
    pp = PdfPages('Charts/Exam_Supervision_Chart.pdf')
    pp.savefig()
    pp.close()


emp = []
emp_index = 0
exams = []
classroom = []

with open('src/date.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        exams.append(row)
del(exams[0])

with open('src/supervisor.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        emp.append(row[0])
del(emp[0])

with open('src/classroom.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        classroom.append(row[0])
del(classroom[0])


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

classroom.sort()
pdf_li = []
for x in final_li:
    temp_li = [x[0]]
    x = x[1:]
    x.sort()
    i,j=0,0
    while i < len(x) and j<len(classroom):
        if x[i][0] == classroom[j]:
            temp_li.append(x[i][1])
            i+=1
        else:
            temp_li.append("-")
        j+=1
    pdf_li.append(temp_li)

make_pdf(pdf_li)
