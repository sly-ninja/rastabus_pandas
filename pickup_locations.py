import platform
from bs4 import BeautifulSoup
from selenium import webdriver

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

url = 'https://adayinlatours.zaui.net/modules/webBooking/index.php?action=Details&id=1'

browser.get(url)


soup = BeautifulSoup(browser.page_source, "html.parser")


addresses = [str(x.text) for x in soup.find(id="pickupId").find_all('option')]


addresses.split(',')

#print(addresses)



browser.quit()

