#!/usr/bin/python

# import library used to query a website
from urllib2 import Request, urlopen, URLError, HTTPError

# import Beautiful soup functions
from bs4 import BeautifulSoup

# import csv library
import csv

# specify url and headers
scrape_url = 'http://infonet-biovision.org/crops-fruits-veg'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
browser_headers = {'User-Agent': user_agent}
browser_data=None

# request url
req = Request(scrape_url,browser_data,browser_headers)

# store url response
page_response = urlopen(req)

# try and catch url and http error 
try: 
    page_response
except HTTPError as e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code: ', e.code
except URLError as e:
    print 'We failed to reach a server.'
    print 'Reason: ', e.reason
else:
    read_html = page_response.read()

    # parse html page via Beautiful Soup
    soup = BeautifulSoup(read_html,'lxml')

    # prettify output
    # print soup.prettify()
    tags = soup.find_all('td','views-field-title')
    
    # create and open csv file
    f = open("infonet-plant-health-links.csv","w")
    data_file = csv.writer(f)
    data_file.writerow(['No.', 'URL'])
    
    # counter
    count = 0
    
    # loop through tags
    for tag in tags:
        infonet_url = 'http://infonet-biovision.org'
        td_content =  tag.contents
        
        # remove new line and space characters
        td_content.remove(" ")
        td_content.remove("\n")
       
        for child in tag.contents:
            final_url = infonet_url + child['href']
            count += 1
            data_file.writerow([count, final_url])

    f.close()
    
    # get number of tags
    print len(tags)