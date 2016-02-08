def dateConv(dateString):
  dateString=dateString.replace('-','')

  dateString=dateString.replace('Jan','01')
  dateString=dateString.replace('Feb','02')
  dateString=dateString.replace('Mar','03')
  dateString=dateString.replace('Apr','04')
  dateString=dateString.replace('May','05')
  dateString=dateString.replace('Jun','06')
  dateString=dateString.replace('Jul','07')
  dateString=dateString.replace('Aug','08')
  dateString=dateString.replace('Sep','09')
  dateString=dateString.replace('Oct','10')
  dateString=dateString.replace('Nov','11')
  dateString=dateString.replace('Dec','12')

  dd=dateString[:2]

  mm=dateString[2:4]
  yy=dateString[-2:]
  yy='20'+yy

  dateString=yy+mm+dd+'000000'

  return dateString

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