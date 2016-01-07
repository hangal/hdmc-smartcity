import csv
input = open('all_works_14_11_15.csv', 'rU')
output = open('all_works_14-15.csv', 'wb')
writer = csv.writer(output)
for row in csv.reader(input):
	writer.writerow(row)
	break
input.next()
for row in csv.reader(input):
    year=int(row[16][-2:])
    if(year>13):
    	writer.writerow(row)
input.close()
output.close()