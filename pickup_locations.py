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


addresses = get_address_list()
#print(*addresses, sep='\n')


cities = ['Beverly Hills', 'Century City', 'Hollywood', 'LAX', 'Marina Del Rey', 'North Hollywood', 'Santa Monica', 'Venice', 'West Hollywood', 'Westwood']

def group_pickup_locations(addresses):
    
    location_groups = dict.fromkeys(cities, [])
    
    for address in addresses:
        if address in cities:
            location_groups[city].append(address)
    
    return location_groups

location_groups = group_pickup_locations(addresses)
print(location_groups)


cities = ['Beverly Hills', 'Westwood']
location_groups = dict.fromkeys(cities, [])
for city in cities:
    print('CITY: ', city)
    for address in addresses:
        print('ADDRESS: ', address)
        if city in address:
            print('HERE', city)
            location_groups[city].append(address)
        else:
            print('FALSE')
            
            
cities = ['Beverly Hills', 'Westwood']
location_groups = dict.fromkeys(cities, [])       
for address in addresses:
    print('ADDRESS: ', address)
    for city in cities:
        print('CITY: ', city)
        if city in address:
            print('HERE', city)
            location_groups[city].append(address)
            print('END')
        else:
            print('NOPE')



#    if any(city in address for city in cities):

