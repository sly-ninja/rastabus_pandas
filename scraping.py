#soup = BeautifulSoup(html_doc, 'html.parser')


#==============================================================================
# from bs4 import BeautifulSoup
# 
# with open("https://adayinlatours.zaui.net/main.php.html") as fp:
#     soup = BeautifulSoup(fp)
# 
# soup = BeautifulSoup("<html>data</html>")
# 
# print(soup.prettify())
# 
#==============================================================================



#==============================================================================
# 
#  1
# down vote
# 	
# 
# 
# from BeautifulSoup import *
# 
# url='http://python-data.dr-chuck.net/known_by_Eesa.html'
# counts=raw_input('Enter number of pages to jump: ')
# counts=int(counts)
# pos=raw_input('Enter position: ')
# pos=int(pos)
# y1= list()
# y2=list()
# count=0
# while True:
#    data=urllib.urlopen(url).read()
#    soup= BeautifulSoup(data)
#==============================================================================
import urllib
import pandas as pd
from bs4 import BeautifulSoup
import time
import datetime
import json

i = '7/25/2017'
time_input = str( int(time.mktime(datetime.datetime.strptime(i, "%m/%d/%Y").timetuple())) )

url = 'https://adayinlatours.zaui.net/modules/reports/reportsDailyPickupList.php?type=dailyPickupList&start=' + time_input
page = urllib.request.urlopen(url).read()

# convert json text to python dictionary
data = json.loads(page)
print(data)




soup = BeautifulSoup(page, 'html.parser')
df = soup.find('table', {'id': 'dailyManifest'})
print(df)


#<table class="LS-pickupListMainTable tablesorter" showrownumbers="" id="dailyManifest" width="100%" cellspacing="1" cellpadding="1" border="0">














