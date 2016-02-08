import csv, os

from commonFunctions import putCommas
from commonFunctions import dateConv

def workdetails(argv):

    workIDList =[]
    filepath = argv[2].split('root/',1)[0]+'data/HD-works-details-2014-15.csv'
    #print filepath
    with open(filepath, 'rU') as f:
        csvHandle = csv.reader(f)
        csvHandle.next()

        for row in csvHandle:
            wid = int(row[0])
            if wid not in workIDList:
                workIDList.append(wid)

    for number in workIDList:
        rowTotal=0
        amtTotal=0
        with open(filepath, 'rU') as f:
            reader = csv.reader(f)
            reader.next()
            for row in reader:
                if int(row[0])==number:
                    rowTotal+=1
                    try:
                        amtTotal=amtTotal+int(float(row[2])*float(row[5].replace(',','')))
                    except:
                        pass

        amtTotalstr=putCommas(amtTotal)
        rowTotalstr=putCommas(rowTotal)

        with open(os.path.join(argv[2],'worknum','work_'+str(number)+'.html'), 'w+') as k:
            print('Generating HTML for work ID: ' + str(number))
            #print 'Total amount: ' + amtTotalstr
            #print 'Total number of rows: ' + rowTotalstr
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
                    }

                    .scrollup {
                    width: 80px;
                    height: 40px;
                    position: fixed;
                    bottom: 50px;
                    right: 100px;
                    text-indent: 0px
                    border-radius: 20px;
                    border-color:black;
                    border-style:solid;
                    border-width:1px;
                    text-align:center;
                    padding-top:10px;
                    color:black;  
                    background-color:white;
                    }
                    <script>
    $(document).ready(function () {

        $(window).scroll(function () {
            if ($(this).scrollTop() > 100) {
                $('.scrollup').fadeIn();
            } else {
                $('.scrollup').fadeOut();
            }
        });

        $('.scrollup').click(function () {
            $("html, body").animate({
                scrollTop: 0
            }, 600);
            return false;
        });

    });
    </script>


                    </style>\n<title>Smart City</title>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<script src=\"../commonfiles/sorttable.js\"></script>\n<link rel=\"stylesheet\" href=\"../commonfiles/bootstrap.css\">\n<script src=\"../commonfiles/jquery.min.js\"></script>\n<script src=\"../commonfiles/bootstrap.min.js\"></script>\n
                    
                    </head>\n<body>\n<div class=\"container\">\n<img src="../images/hdmc-logo.png" width="140em" height="140em" style="display:inline-block; margin-right:1em; margin-left:7em;">\n
    <h2 style=\"text-align:center; display:inline-block;\"><a href="../all_works/allWorks.html">Hubballi Dharwad Smart Cities Project</a></h2>\n
    <img src="../images/smartcitylogo.jpg" width="150em" height="150em" style="display:inline-block; margin-left:1em; margin-top:1.2em;">""")
      
            k.write("""<h4 style="display:inline-block;"> Total number of works: """+rowTotalstr+"""</h4>""")
            k.write("""<h4 style="display:inline-block; margin-left:3em;"> Total amount spent: &#8377 """+amtTotalstr+"""</h4>""")

      
            k.write("""
            <table class=\"table table-responsive sortable\">\n
            <thead>\n
            <tr>\n
            <th style=\"width:5%\">Sl no.</th>\n
            <th style=\"width:48%\">Work Details</th>\n
            <th>Measurement</th>\n
            <th>Unit</th>\n
            <th>Rate</th>\n
            <th>Total Amount</th>\n
            </tr>\n
            </thead>\n
            <tbody>
            <a href="#" class="scrollup">Go to top</a>
            """)

            with open(filepath, 'rU') as f:
                csvHandle = csv.reader(f)
                csvHandle.next()
                i=1
                for row in csvHandle:
                    if int(row[0]) == number:
                        
                        k.write('<tr>')

                        #serial number
                        k.write('<td class = \"span1\">' + str(i) + '</td>') 

                        #work details           
                        k.write('<td>' + row[3] + '</td>')

                        #measurement                    
                        k.write('<td>' + row[2] + '</td>')

                        #unit
                        k.write('<td>' + row[4] + '</td>')  

                        #rate
                        k.write('<td>' + row[5] + '</td>')

                        #total
                        try:
                            k.write('<td>' + str(float(row[2])*float(row[5].replace(',',''))) + '</td>')
                        except:
                            pass

                        k.write('</tr>')
                        i+=1

            k.write("</tbody>\n</table>\n</div>\n</body>\n</html>")