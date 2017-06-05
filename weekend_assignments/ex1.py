import csv

with open('write.csv','wb') as csv_writefile:
    writer = csv.writer(csv_writefile)
    with open('FL_insurance_sample (1).csv','rb') as csv_data:
        read_data=csv.reader(csv_data)
        for row in read_data:
            writer.writerow([row[0],row[3],row[4],row[5],row[7],row[9]])






























  









