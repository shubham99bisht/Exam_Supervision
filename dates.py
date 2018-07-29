import csv

def write_dates_csv(lis):
    with open('date.csv','a',newline='') as csvfile:
      date_writer = csv.writer(csvfile, delimiter=',')
      date_writer.writerow(lis)
