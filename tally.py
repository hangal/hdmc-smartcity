import csv, sys, os
from operator import itemgetter
from heapq import nlargest

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

#sys.argv
def index(argv,top50contractorsIDList,top50amount):

    print top50contractorsIDList
    print top50amount

    with open(os.path.join(argv[2],'allworks','index.html'), 'w+') as k:
        k.write("""<!DOCTYPE html>\n
            <html lang=\"en\">\n
            <head>\n
            <title>Smart City</title>\n
            <meta charset=\"utf-8\">\n
            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n
            <script src=\"../commonfiles/sorttable.js\"></script>\n
            <link rel=\"stylesheet\" href=\"../commonfiles/bootstrap.css\">\n
            <script src=\"../commonfiles/jquery.min.js\"></script>\n
            <script src=\"../commonfiles/bootstrap.min.js\"></script>\n
            <script src=\"../commonfiles/addons.js\"></script>\n
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/modules/exporting.js"></script>

            </head>\n<body>\n<div class=\"container\">\n<img src="../images/hdmc-logo.png" width="140em" height="140em" style="display:inline-block; margin-right:1em; margin-left:7em;">\n
            <h2 style=\"text-align:center; display:inline-block;\"><a href="../allworks/allworks.html">Hubballi Dharwad Smart Cities Project</a></h2>\n
            <img src="../images/smartcitylogo.jpg" width="150em" height="150em" style="display:inline-block; margin-left:1em; margin-top:1.2em;">
            <a href="#" class="scrollup">Go to top</a><div id="chartallworks" style="width:100%; height:400px;"></div>
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

        
        with open(argv[1], 'rU') as f:
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

            k.write("""<div id="chartcontractors" style="width:100%; height:400px;"></div>""")

            k.write("""
            <table class=\"table table-responsive sortable\" id="myTable" style="margin-top:2em">\n
            <thead>\n
            <tr>\n
            <th>Ward</th>\n
            <th>In progress</th>\n
            <th> Total works</th>\n
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
            with open(argv[1], 'rU') as f:
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



                k.write("<tr>")
                k.write("<td><a href=\"../wardworks/ward_"+row[1]+".html\" target=\"_blank\">"+str(ward)+"</a></td>")
                k.write("<td>"+inprogressWorksTotalstr+"</td>")
                k.write("<td>"+rowTotalstr+"</td>")
                k.write("<td>"+contractorsTotal+"</td>")
                k.write("<td>"+amtTotalstr+"</td>")
                k.write("</tr>")

                wardWorksDict[str(ward)]=rowTotalstr

                wardWiseAmount.append(amtTotal)
                wardWiseCompleted.append(completedWorksTotal)
                wardWiseInprogress.append(inprogressWorksTotal)
                wardWiseWorksTotal.append(rowTotal)

        k.write("</tbody>\n</table>\n")
    
        k.write("""
        <script>
        $(function () { 
        $('#chartallworks').highcharts({
            chart: {
                type: 'column'
            },
            title: {
                text: 'Ward wise dashboard'
            },
            credits: {
                enabled: true
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
                data: """ + str(wardWiseWorksTotal) + """,
                visible: false
            }, {
                name: 'Completed works',
                data: """ + str(wardWiseCompleted) + """,
                visible: false
            }, {
                name: 'In progress works',
                data: """ + str(wardWiseInprogress) + """,
                
            }, {
                name: 'Total amount spent',
                data: """ + str(wardWiseAmount) + """,
                visible: false
            }]
        });
    
        $('#chartcontractors').highcharts({
            chart: {
                type: 'column'
            },
            title: {
                text: 'Top 50 Contractors by Amount'
            },
            credits: {
                enabled: true
            },
            xAxis: {
                categories: """ + str(top50contractorsIDList) + """
            },
            yAxis: {
                title: {
                    text: 'Magnitude'
                }
            },
            series: [{
                name: 'Total works',
                data: """ + str(top50amount) + """,
                visible: true
            
            }]
        });
    });

    </script>""")
        k.write("</tbody>\n</table>\n</div>\n</body>\n</html>")
        k.close()

def contractor(argv):
    contractorIDList=[]
    top50contractorsIDList=[]
    contractorID_amount={}
    amountList=[]

    with open(argv[1], 'rU') as f:
        reader=csv.reader(f)
        for row in reader:
            if int(row[12]) not in contractorIDList:
                contractorIDList.append(int(row[12]))

    print(len(contractorIDList))

    for contractorID in contractorIDList:
        
        with open(argv[1], 'rU') as f:
            reader = csv.reader(f)
            #reader.next()
            rowTotal=0
            amtTotal=0
            completedWorksTotal=0
            inprogressWorksTotal=0
            for row in reader:
                #print(row[12])
                #print contractorID
                #time.sleep(1)
                if int(row[12])==contractorID:
                    rowTotal+=1
                    amtTotal=amtTotal+int(row[14])
                    if row[17] == 'completed':
                        completedWorksTotal+=1
                    if row[17] == 'inprogress':
                        inprogressWorksTotal+=1

        amtTotalstr=putCommas(amtTotal)
        rowTotalstr=putCommas(rowTotal)
        completedWorksTotalstr=putCommas(completedWorksTotal)
        inprogressWorksTotalstr=putCommas(inprogressWorksTotal)
        if (amtTotal not in amountList):
            amountList.append(amtTotal)
        contractorID_amount[amtTotal]=contractorID



    amountList.sort()
    print('-----------------------------')
    print(nlargest(50,amountList))
    top50amount=(nlargest(50,amountList))
    for number in amountList:
        top50contractorsIDList.append(contractorID_amount[number])
    return top50contractorsIDList, top50amount

top50contractorsIDList, top50amount = contractor(sys.argv)
index(sys.argv,top50contractorsIDList,top50amount)
