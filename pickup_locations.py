from scraping_class import Scraping

def get_address_list():
    
    url = 'https://adayinlatours.zaui.net/modules/webBooking/index.php?action=Details&id=1'
    
    obj = Scraping(url)
    soup, browser = obj.read_url()
    
    addresses = [str(x.text) for x in soup.find(id='pickupId').find_all('option')]
    keywordFilter = ['*', '1400 Ocean Ave']
    addresses =  [sent for sent in addresses if not any(word in sent for word in keywordFilter)]
    del addresses[0]
    
    browser.quit()
    
    return addresses

address_list = get_address_list()
