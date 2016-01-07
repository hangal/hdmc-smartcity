import csv

with open('output.txt', 'w+') as k:

	with open('all_works_14_11_15.csv', 'rU') as f:
	    reader = csv.reader(f)
	    for row in reader:
	    	#print row[1]
	        if row[1] == '44':
	        	k.write('<tr>')
	        	k.write('<td>' + row[10] + '</td>')
	        	k.write('<td>' + row[4] + '</td>')
	        	k.write('<td>' + row[11] + '</td>')
	        	k.write('</tr>')

	        	"""
	        	<tr>
			        <td>John</td>
			        <td>Doe</td>
			        <td>john@example.com</td>
		      	</tr>
		      	"""