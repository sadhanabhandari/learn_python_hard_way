import csv

with open('project2.csv','wb') as csv_writefile:
     writer = csv.writer(csv_writefile)
     with open('FL_insurance_sample (1).csv','rb') as csv_readfile:
         reader=csv.reader(csv_readfile)
         a = next(reader)
         print a
         #for row in reader:
          #   print row[0]
             #writer.writerow([row[0]])
            #writer.writerow([','.join(row)])



