import csv, sys
from operator import itemgetter

def putCommas(num):
  numUlta = str(num)[::-1]
  revnumstr = str(numUlta)
  newstr = revnumstr[:3]+','+revnumstr[3:5]+','+revnumstr[5:7]+','+revnumstr[7:]
  retstr=newstr[::-1]
  for k in retstr:
    if (k==','):
      retstr=retstr.replace(',','',1)
    else:
      break
  return retstr

#sys.argv[1]
with open(sys.argv[2], 'w+') as k:
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
    </style>\n<title>Smart City</title>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n<script src=\"../common_files/sorttable.js\"></script>\n<link rel=\"stylesheet\" href=\"../common_files/bootstrap.css\">\n<script src=\"../common_files/jquery.min.js\"></script>\n<script src=\"../common_files/bootstrap.min.js\"></script>\n
    </script>
    <script src="https://code.highcharts.com/highcharts.js"></script>
    <script src="https://code.highcharts.com/modules/exporting.js"></script>

    <script>
    function worksTotal(){
    var table = document.getElementById("myTable");
    var x = table.rows.length;
    document.getElementById("totalWorks").innerHTML = x
    }
    </script>
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
    </head>\n<body>\n<div class=\"container\">\n<img src="../images/hdmc-logo.png" width="140em" height="140em" style="display:inline-block; margin-right:1em; margin-left:7em;">\n
    <h2 style=\"text-align:center; display:inline-block;\"><a href="../all_works/allWorks.html">Hubballi Dharwad Smart Cities Project</a></h2>\n
    <img src="../images/smartcitylogo.jpg" width="150em" height="150em" style="display:inline-block; margin-left:1em; margin-top:1.2em;">
    <a href="#" class="scrollup">Go to top</a><div id="chart" style="width:100%; height:400px;"></div>
    """)

    rowTotal=0
    amtTotal=0
    contractorsList=[]
    wardList=[]
    workTypeIDList=[]
    wardWorksDict={}
    wardWiseCompleted=[]
    wardWiseInprogress=[]
    wardWiseAmount=[]
    wardWiseWorksTotal=[]

    #Example row from csv
    #"36,836.00",103,1,35,"Water Supply arrangement to unserved areas in Hubli city under HDMC-SFC Grants.",2010-11£ÉÃ ¸Á°£À°è JZï.r.JA.¹- J¸ï.J¥sï.¹ UÁåAn£À°è ºÀÄ§â½î £ÀUÀgÀzÀ ¸ÉÃªÁgÀ»vÀ ¥ÀæzÉÃ±ÀUÀ½UÉ ¤ÃgÀÄ ¸ÀgÀ§gÁdÄ PÀ°à¸ÀÄªÀ PÀÄjvÀÄ.,"950,000.00",05-Jan-11,05-Jan-11,950000,05-Jan-11,EE Karnataka Water Boad Dharwad,4713,0,950000,05-Jan-11,05-Jan-11,completed,2011,SFC-Water Supply Scarcity,Capital,45,,1,2010-11ನೇ ಸಾಲಿನಲ್ಲಿ ಎಚ್.ಡಿ.ಎಂ.ಸಿ- ಎಸ್.ಎಫ್.ಸಿ ಗ್ಯಾಂಟಿನಲ್ಲಿ ಹುಬ್ಬಳ್ಳಿ ನಗರದ ಸೇವಾರಹಿತ ಪ್ರದೇಶಗಳಿಗೆ ನೀರು ಸರಬರಾಜು ಕಲ್ಪಿಸುವ ಕುರಿತು.
    
    with open(sys.argv[1], 'rU') as f:
        reader = csv.reader(f)
        #reader.next()
        for row in reader:
            rowTotal+=1
            amtTotal=amtTotal+int(row[14])
            if row[11] not in contractorsList:
              contractorsList.append(row[11])
            try:
                if int(row[1]) not in wardList:
                    wardList.append(int(row[1]))
            except:
                pass
            if int(row[2]) not in workTypeIDList:
                workTypeIDList.append(int(row[2]))

            amtTotalstr=putCommas(amtTotal)
            rowTotalstr=putCommas(rowTotal)
            contractorsTotal=putCommas(len(contractorsList))  

        wardList.sort()
            
        k.write("""<h4 style="display:inline-block;margin-left:5em"> Total number of works: """+rowTotalstr+"""</h4>""")
        #k.write("""<h4 style="display:inline-block; margin-left:7em;"> Completed works: """+completedWorksTotalstr+"""</h4>""")
        #k.write("""<h4 style="display:inline-block; margin-left:7em;"> In progress works: """+inprogressWorksTotalstr+"""</h4>""")
        k.write("""<h4 style="display:inline-block; margin-left:5em;"> Total amount spent: &#8377 """+amtTotalstr+"""</h4>""")
        k.write("""<h4 style="display:inline-block; margin-left:3.5em;"> Total number of contractors: """+contractorsTotal+"""</h4>""")

        k.write("""
        <table class=\"table table-responsive sortable\" id="myTable" style="margin-top:2em">\n
        <thead>\n
        <tr>\n
        <th>Ward</th>\n
        <th>In progress/ Total works</th>\n
        <th>Number of contractors</th>\n
        <th>Total amount</th>\n
        </tr>\n
        </thead>\n
        <tbody>
        """)

    for ward in wardList:
        rowTotal=0
        amtTotal=0
        completedWorksTotal=0
        inprogressWorksTotal=0
        contractorsByWardList=[]
        #reader.next()
        #print(ward)
        #print(type(ward))
        with open('all_works_2014_15.csv', 'rU') as f:
            reader=csv.reader(f)
            #reader.next()
            for row in reader:
                #print(row[1])
                #print(type(row[1]))
                if((row[1])==str(ward)):
                    rowTotal+=1
                    #print(rowTotal)
                    amtTotal=amtTotal+int(row[14])
                    if row[11] not in contractorsByWardList:
                        contractorsByWardList.append(row[11])
                    if row[17] == 'completed':
                        completedWorksTotal+=1
                    if row[17] == 'inprogress':
                        inprogressWorksTotal+=1

            amtTotalstr=putCommas(amtTotal)
            rowTotalstr=putCommas(rowTotal)
            completedWorksTotalstr=putCommas(completedWorksTotal)
            inprogressWorksTotalstr=putCommas(inprogressWorksTotal)
            contractorsTotal=putCommas(len(contractorsByWardList))

            print('Ward: ' + str(ward))
            print('Amount: ' + amtTotalstr)
            print('Works total: ' + rowTotalstr)
            print('Completed: ' + completedWorksTotalstr)
            print('In progress: ' + inprogressWorksTotalstr)
            print('Number of contractors: ' + contractorsTotal)
            print('\n')

            k.write("<tr>")
            k.write("<td>"+str(ward)+"</td>")
            k.write("<td>"+inprogressWorksTotalstr+'/'+ rowTotalstr+"</td>")
            k.write("<td>"+contractorsTotal+"</td>")
            k.write("<td>"+amtTotalstr+"</td>")
            k.write("</tr>")

            wardWorksDict[str(ward)]=rowTotalstr

            wardWiseAmount.append(amtTotal)
            wardWiseCompleted.append(completedWorksTotal)
            wardWiseInprogress.append(inprogressWorksTotal)
            wardWiseWorksTotal.append(rowTotal)

    k.write("</tbody>\n</table>\n")
    k.write("<h4>Top 50 contractors</h4>")
    k.write("""
        <table class=\"table table-responsive sortable\" id="myTable" style="margin-top:2em">\n
        <thead>\n
        <tr>\n
        <th>Ward</th>\n
        <th>Contractor</th>\n
        <th>In progress/Total works</th>\n
        <th>Total amount</th>\n
        </tr>\n
        </thead>\n
        <tbody>
        """)
    count=len(contractorsList)
    contractorAmountList=[]
    for contractor in contractorsList:
        conRowTotal=0
        conAmtTotal=0
        conCompletedWorksTotal=0
        conInprogressWorksTotal=0
        conWorksTotal=[]
        conAmtTotalList=[]
        #reader.next()
        #print(ward)
        #print(type(ward))
        with open('all_works_2014_15.csv', 'rU') as f:
            reader=csv.reader(f)
            #reader.next()
            for row in reader:
                #print(row[1])
                #print(type(row[1]))
                if((row[11])==(contractor)):
                    conRowTotal+=1
                    #print(rowTotal)
                    conAmtTotal=conAmtTotal+int(row[14])
                    if row[17] == 'inprogress':
                        conInprogressWorksTotal+=1

            conWorksTotal.append(conRowTotal)
            conAmtTotalList.append(conAmtTotal)
            conamttemp=[contractor,conAmtTotal]
            contractorAmountList.append(conamttemp)
            conAmtTotalstr=putCommas(conAmtTotal)
            conRowTotalstr=putCommas(conRowTotal)
            conInprogressWorksTotalstr=putCommas(conInprogressWorksTotal)
            #contractorsTotal=putCommas(len(contractorsByWardList))


            print('Contractor: ' + contractor)
            print('\n')
            
            k.write("<tr>")
            k.write("<td>"+str(ward)+"</td>")
            k.write("<td>"+conInprogressWorksTotalstr+'/'+conRowTotalstr+"</td>")
            k.write("<td>"+contractor+"</td>")
            k.write("<td>"+conAmtTotalstr+"</td>")
            k.write("</tr>")

            
    conAmtTotalList.sort()
    print(contractorAmountList)

    contractorAmountList=sorted(contractorAmountList, key=itemgetter(1))
    print(contractorAmountList)

    k.write("""<script>
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
    </script>""")

    k.write("""
    <script>
    $(function () { 
    $('#chart').highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: 'Ward wise statistics'
        },
        xAxis: {
            categories: """ + str(wardList) + """
        },
        yAxis: {
            title: {
                text: 'Magnitude'
            }
        },
        series: [{
            name: 'Total works',
            data: """ + str(wardWiseWorksTotal) + """
        }, {
            name: 'Completed works',
            data: """ + str(wardWiseCompleted) + """
        }, {
            name: 'In progress works',
            data: """ + str(wardWiseInprogress) + """
        }, {
            name: 'Total amount spent',
            data: """ + str(wardWiseAmount) + """
        }]
    });
});
</script>""")
    k.write("</tbody>\n</table>\n</div>\n</body>\n</html>")
k.close()