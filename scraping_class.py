import platform
from bs4 import BeautifulSoup
from selenium import webdriver
    
class Scraping:
     
    def __init__(self, url):
        self.url = url

    def read_url(self):
        
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
        
        # url = 'https://adayinlatours.zaui.net/modules/webBooking/index.php?action=Details&id=1'
        
        browser.get(self.url)
        
        soup = BeautifulSoup(browser.page_source, "html.parser")
        
        return soup, browser






