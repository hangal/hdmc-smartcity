import csv

for contractorID in range(1,8033):
	print("Generating HTML for file " + str(contractorID))
	with open('C:\Projects\HDMC\scripts\htmlFiles\contractors\contractor'+str(contractorID)+'.html', 'w+') as k:
		k.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<title>Smart City</title>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<link rel=\"stylesheet\" href=\"http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css\">\n<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js\"></script>\n<script src=\"http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js\"></script>\n</head>\n<body>\n<div class=\"container\">\n<h2>All works by "+ str(contractorID) + "</h2>\n<p>Description here</p>\n<table class=\"table table-responsive\">\n<thead>\n<tr>\n<th style=\"width:5%\">Ward</th>\n<th style=\"width:48%\">Work Description</th>\n<th>Work Order Date</th>\n<th>Work Completion Date</th>\n<th style=\"width:10%\">Contractor</th>\n<th>Amount Sanctioned</th>\n</tr>\n</thead>\n<tbody>")

		with open('all_works_14_11_15.csv', 'rU') as f:
		    reader = csv.reader(f)
		    for row in reader:
		    	#print row[1]
		        if row[12] == str(contractorID):
		        	k.write('<tr>')
		        	k.write('<td class = \"span1\">' + str(contractorId) + "</td>")        	
                     #contractorId
		        	if (len(row[4])<=3):
		        		k.write('<td>Info not available</td>')			
#work description
		        	else:
		        		k.write('<td>' + row[4] + '</td>')
		        	k.write('<td>' + row[15] + '</td>')					#work order date
		        	k.write('<td>' + row[16] + '</td>')					#work completion date
		        	k.write('<td>' + row[11] + '</td>')					#contractor
		        	k.write('<td>' + row[14] + '</td>')					#amount sanctioned
		        	k.write('</tr>')

		        	"""
		        	<tr>
				        <td>John</td>
				        <td>Doe</td>
				        <td>john@example.com</td>
			      	</tr>
			      	"""

		k.write("</tbody>\n</table>\n</div>\n</body>\n</html>")