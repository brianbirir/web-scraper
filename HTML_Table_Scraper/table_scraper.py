# Web Scraper for HTML table

import requests
import bs4
import csv

# open file
 # create and open csv file
f = open("kenya_wards.csv","w")
data_file = csv.writer(f)
data_file.writerow(['WardName', 'Constituency','County','WardPop2009','AreaSqKms','VoterTarget','RegVoters','Voters %'])

# get elections database page
res = requests.get('http://kenyaelectiondatabase.co.ke/?page_id=1010')

res.raise_for_status()

# parse HTML
parseHTML = bs4.BeautifulSoup(res.text,'lxml')

# Create an object of the first object that is id tablepress-13
wards_tbl = parseHTML.find(id='tablepress-13')

# find all tr and skip the first one
for ward_row in wards_tbl.find_all('tr')[1:]:    
    
    # get columns
    ward_cols = ward_row.find_all('td')
    
    # store data in list
    ward_data = []
    
    for td in ward_cols:
        text = ''.join(td)
        utftext = str(text.encode('utf-8'))
        ward_data.append(utftext)

    data_file.writerow(ward_data)
    #print ward_data

f.close()