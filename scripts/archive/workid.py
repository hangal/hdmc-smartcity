import csv

for workID1 in range(50000,70000):
	print("Generating HTML for file " + str(workID1))
	k = open('C:\Projects\HDMC\scripts\htmlFiles\worktype/work_'+str(workID1)+'.html', 'w+') 
	k.write("""<!DOCTYPE html>\n<html lang=\"en\">\n<head><style>table.sortable th:not(.sorttable_sorted):not(.sorttable_sorted_reverse):not(.sorttable_nosort):after {content: \" \\25B4\\25BE\"}display: inline-block;
		  width: 24px;
		  height: 24px;
		}
		th.sorttable_sorted::after {
		  background: url(up.png);
		  background-size: contain;
		}
		th.sorttable_sorted_reverse::after {
		  background: url(down.png);
		  background-size: cover;
		}</style>\n<title>Smart City</title>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<script src=\"sorttable.js\"></script>\n<link rel=\"stylesheet\" href=\"http://bootswatch.com/cosmo/bootstrap.css\">\n<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js\"></script>\n<script src=\"http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js\"></script>\n</head>\n<body>\n<div class=\"container\">\n<h2 style=\"text-align:center\">Hubballi Dharwad Smart Cities Project</h2>\n<p style=\"text-align:center\"></p>""")
		  
	k.write("""<h4> Total number of works: </h4>""")
	  
	k.write("""
	    <table class=\"table table-responsive sortable\">\n
	    <thead>\n
	    <tr>\n
	    <th style=\"width:5%\">Ward</th>\n
	    <th style=\"width:48%\">Work Description</th>\n
	    <th>Work Order Date</th>\n
	    <th>Work Completion Date</th>\n
	    <th>Work Type</th>\n
	    <th>Source of Income</th>\n
	    <th style=\"width:7%\">Contractor</th>\n
	    <th>Amount Sanctioned</th>\n
	    <th>Status</th>\n
	    </tr>\n
	    </thead>\n
	    <tbody>
	    """) 

	with open('HD-works-details-2014-15.csv', 'rU') as f:
	    reader = csv.reader(f)
	    for row in reader:
	    	workID1 = row[0][:-3].replace(',','')
		    #workID1 = int(workID)
	        if row[1] == str(workID1):
	     		k.write('<tr>')
			  	#k.write('<td>' + str(workID1) + '</td>')        	
			    k.write('<td>' + row[3] + '</td>')					#work details
			    k.write('<td>' + row[5] + '</td>')					#amount sanctioned
		        k.write('</tr>')   

        
	k.write("</tbody>\n</table>\n</div>\n</body>\n</html>")