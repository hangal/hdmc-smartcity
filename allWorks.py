#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import csv, os, sys
import wardworks
import contractor
import worktype
from operator import itemgetter
#import workdetails

def putCommas(num):
  numUlta = str(num)[::-1]
  revnumstr = str(numUlta)
  newstr = revnumstr[:3]+','+revnumstr[3:5]+','+revnumstr[5:7]+','+revnumstr[7:9]+','+revnumstr[9:11]
  retstr=newstr[::-1]
  for k in retstr:
    if k==',':
      retstr=retstr.replace(',','',1)
    else:
      break
  return retstr

def index(argv):
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
        $('#chart').highcharts({
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
    });
    </script>""")
        k.write("</tbody>\n</table>\n</div>\n</body>\n</html>")
        k.close()
    print('Home page created!')

def allworks(argv):
  rowTotal=0
  amtTotal=0
  inprogressWorksTotal=0
  completedWorksTotal=0
  contractorsList=[]
  with open(argv[1], 'rU') as f:
        reader = csv.reader(f)
        #reader.next()
        for row in reader:
          rowTotal+=1
          amtTotal=amtTotal+int(row[14])
          if row[11] not in contractorsList:
            contractorsList.append(row[11])
          if row[17] == 'completed':
            completedWorksTotal+=1
          if row[17] == 'inprogress':
            inprogressWorksTotal+=1

        amtTotalstr=putCommas(amtTotal)
        rowTotalstr=putCommas(rowTotal)
        completedWorksTotalstr=putCommas(completedWorksTotal)
        inprogressWorksTotalstr=putCommas(inprogressWorksTotal)
        contractorsTotal=putCommas(len(contractorsList))

  with open(os.path.join(argv[2],'allworks','allworks.html'), 'w+') as k:
    k.write("""<!DOCTYPE html>\n<html lang=\"en\">\n
      <head>
      \n<title>Smart City</title>\n
      <meta charset=\"utf-8\">\n
      <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n
      <script src=\"../commonfiles/sorttable.js\"></script>\n
      <link rel=\"stylesheet\" href=\"../commonfiles/bootstrap.css\">\n
      <script src=\"../commonfiles/jquery.min.js\"></script>\n
      <script src=\"../commonfiles/bootstrap.min.js\"></script>\n
      <script src=\"../commonfiles/addons.js\"></script>\n
  </head>\n<body>\n<div class=\"container\">\n<img src="../images/hdmc-logo.png" width="140em" height="140em" style="display:inline-block; margin-right:1em; margin-left:7em;">\n
  <h2 style=\"text-align:center; display:inline-block;\"><a href="../allworks/allworks.html">Hubballi Dharwad Smart Cities Project</a></h2>\n
  <img src="../images/smartcitylogo.jpg" width="150em" height="150em" style="display:inline-block; margin-left:1em; margin-top:1.2em;"><div class="pull-right" style="margin-top:40px;"><a href="allworks_k.html" target="_blank">ಕನ್ನಡ</a> | <a href="allworks.html" target="_blank">English</a></div>""")
    
    k.write("""<h4 style="display:inline-block;margin-left:5em"> Total number of works: """+rowTotalstr+"""</h4>""")
    k.write("""<h4 style="display:inline-block; margin-left:7em;"> Completed works: """+completedWorksTotalstr+"""</h4>""")
    k.write("""<h4 style="display:inline-block; margin-left:7em;"> In progress works: """+inprogressWorksTotalstr+"""</h4>""")
    k.write("""<h4 style="display:inline-block; margin-left:5em;"> Total amount spent: &#8377 """+amtTotalstr+"""</h4>""")
    k.write("""<h4 style="display:inline-block; margin-left:3.5em;"> Total number of contractors: """+contractorsTotal+"""</h4>""")
    
    k.write("""
      <table class=\"table table-responsive sortable\" id="myTable" style="margin-top:2em">\n
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
      <a href="#" class="scrollup">Go to top</a>
      """) 
    rowTotal=0
    with open(sys.argv[1], 'rU') as f:
        reader = csv.reader(f)
        #reader.next()
        for row in reader:
          #print row[16]
          year=int(row[16][-2:])
          workID = row[0][:-3].replace(',','')
          workID = int(workID)
          #print (workID)
          k.write('<tr>')

          #ward number
          k.write('<td class = \"span1\"><a href=\"../wardworks/ward_'+row[1]+'.html\" target=\"_blank\">' + row[1] + '</a></td>')    
          
          #work description
          if (len(row[4])<=4):
            try:
              k.write('<td><a href=\"../worknum/work_'+str(workID)+'.html\" target=\"_blank\">' + row[24] + '</a></td>')
            except:
              pass     
          else:
            if(row[2] == '1' or row[2] == '2' or row[2] == '3'):
              k.write('<td><a href=\"../worknum/work_'+str(workID)+'.html\" target=\"_blank\">' + row[4] + '</a></td>')
            else:
              k.write('<td>'+ row[4] + '</td>')
          
          #work order date
          k.write('<td>' + row[15] + '</td>')         

          #work completion date
          k.write('<td>' + row[16] + '</td>')     

          #type of work
          k.write('<td><a href=\"../worktype/worktype_'+row[2]+'.html\" target=\"_blank\">' + row[20] + '</a></td>') 

          #source of income
          k.write('<td>' + row[19] + '</td>')   
          
          #contractor
          k.write('<td><a href=\"../contractors/contractor_'+row[12]+'.html\" target=\"_blank\">' + row[11] + '</a></td>')         
          
          #amount
          amt = int(row[14])
          amtstr=putCommas(amt)
          k.write('<td style="text-align:center;">' + amtstr + '</td>') 

          #status
          try:
            if(row[17]=="completed"):
              k.write('<td style="color:#43ac6a;">' + row[17][0].upper()+row[17][1:].lower() + '</td>') 
            else:
              k.write('<td style="color:#d32a0e;">' + row[17][0].upper()+row[17][1:].lower() + '</td>') 
          except:
            pass

          k.write('</tr>')   

          rowTotal+=1   

    k.write("</tbody>\n</table>\n</div>\n")
    k.write("</body>\n</html>")


  print("Done generating all works!") 

if not os.path.exists(os.path.join(sys.argv[2],'allworks')):
  os.makedirs(os.path.join(sys.argv[2],'allworks'))
if not os.path.exists(os.path.join(sys.argv[2],'wardworks')):
  os.makedirs(os.path.join(sys.argv[2],'wardworks'))
if not os.path.exists(os.path.join(sys.argv[2],'worktype')):
  os.makedirs(os.path.join(sys.argv[2],'worktype'))
if not os.path.exists(os.path.join(sys.argv[2],'contractors')):
  os.makedirs(os.path.join(sys.argv[2],'contractors'))

index(sys.argv)
allworks(sys.argv)
wardworks.wardworks(sys.argv)
worktype.worktype(sys.argv)
contractor.contractor(sys.argv)
#workdetails()