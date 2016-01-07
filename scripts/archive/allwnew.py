import csv

with open('C:\Projects\HDMC\scripts\htmlFiles/all_works/allWorks.html', 'w+') as k:
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
	
	k.write("""<h4> Total number of works: <div id="totalnum"></div></h4>""")
	k.write("""<div class="dropdown">
  <button class="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Select Ward<span class="caret"></span></button>
  <ul class="dropdown-menu">
    <li><a href="#">1</a></li>
    <li><a href="#">2</a></li>
    <li><a href="#">3</a></li>
    <li><a href="#">4</a></li>
    <li><a href="#">5</a></li>
    <li><a href="#">6</a></li>
    <li><a href="#">7</a></li>
    <li><a href="#">8</a></li>
    <li><a href="#">9</a></li>
    <li><a href="#">10</a></li>
    </ul>
	</div>
    """)

	k.write("<table class=\"table table-responsive sortable\">\n<thead>\n<tr>\n<th style=\"width:5%\">Ward</th>\n<th style=\"width:48%\">Work Description</th>\n<th>Work Order Date</th>\n<th>Work Completion Date</th>\n<th style=\"width:7%\">Contractor</th>\n<th>Amount Sanctioned</th>\n</tr>\n</thead>\n<tbody>")	

	with open('all_works_14-15.csv', 'rU') as f:
	    reader = csv.reader(f)
	    reader.next()
	    for row in reader:
	    	year=int(row[16][-2:])
        	workID = row[0][:-3].replace(',','')
        	workID = int(workID)
        	print (workID)
        	k.write('<tr>')
        	k.write('<td class = \"span1\"><a href=\"C:\Projects\HDMC\scripts\htmlFiles\ward_works/ward_'+row[1]+'.html\" target=\"_blank\">' + row[1] + '</a></td>')        	#ward number
        	if (len(row[4])<=4):
        		k.write('<td>Info not available</td>')			#work description
        	else:
        		k.write('<td><a href=\"C:\Projects\HDMC\scripts\htmlFiles\worknum/work_'+str(workID)+'.html\" target=\"_blank\">' + row[4] + '</a></td>')
        	k.write('<td>' + row[15] + '</td>')					#work order date

        	k.write('<td>' + row[16] + '</td>')					#work completion date
        	k.write('<td><a href=\"C:\Projects\HDMC\scripts\htmlFiles/contractors/contractor'+row[12]+'.html\" target=\"_blank\">' + row[11] + '</a></td>')					#contractor
        	amt = '{:,}'.format(int(row[14]))
        	k.write('<td>' + amt + '</td>')					#amount sanctioned
        	k.write('</tr>')     	

	k.write("</tbody>\n</table>\n</div>\n")
	k.write("""<script>var rows = document.getElementsByClassName('table table-responsive sortable').getElementsByTagName('tbody')[0].getElementsByTagName('tr').length;
			document.getElementById("totalnum").innerHTML = "sdggrge";	
			</script>""")
	k.write("</body>\n</html>")

print("Done!")  