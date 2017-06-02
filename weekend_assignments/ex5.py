import csv

with open('brand_new.csv','wb') as csv_writefile:
    writer = csv.writer(csv_writefile)
    with open('FL_insurance_sample (1).csv', 'rb') as csv_readfile:
        reader = csv.reader(csv_readfile)
        for row in reader:
            writer.writerow(row[5])

