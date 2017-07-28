import platform
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime

# PhantomJS files have different extensions
# under different operating systems
if platform.system() == 'Windows':
    PHANTOMJS_PATH = './phantomjs.exe'
else:
    PHANTOMJS_PATH = './phantomjs'


# here we'll use pseudo browser PhantomJS,
# but browser can be replaced with browser = webdriver.FireFox(),
# which is good for debugging.
browser = webdriver.PhantomJS(PHANTOMJS_PATH)

i = '7/25/2017'
time_input = str( int(time.mktime(datetime.datetime.strptime(i, "%m/%d/%Y").timetuple())) )
url = 'https://adayinlatours.zaui.net/modules/reports/reportsDailyPickupList.php?type=dailyPickupList&start=' + time_input

browser.get(url)
browser.find_element_by_id('entryu_div').send_keys(user_name)
browser.find_element_by_id('entryp_div').send_keys(password)
browser.find_elements_by_class_name("submitit")[0].click()


browser.get('https://adayinlatours.zaui.net/tmp/2017-07-25-35057.xls')


#time.sleep(5)

# let's parse our html
soup = BeautifulSoup(browser.page_source, "html.parser")
# get all the games
table = soup.find_all('table', {'id': 'dailyManifest'})

# and print out the html for first game
print(table)




browser.quit()


#https://adayinlatours.zaui.net/tmp/2017-07-25-35057.xls

#https://adayinlatours.zaui.net/tmp/2017-07-25-35057.xls