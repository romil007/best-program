#Python Project related to web scrapping
'''In this project input is to be given of which channel do you want and 
   it will in return give recommendation of which pack is vmost useful and viable.'''

from bs4 import BeautifulSoup
#from urllib.request import urlopen,Request
import requests
import pandas as pd
import re
import numpy as np

url = 'https://www.tatasky.com/wps/portal/TataSky/packs/tata-sky-channels'

'''request=Request(url)
response=urlopen(request)
# This is used as urlib method which is modified recently'''

# Packages the request, send the request and catch the response in variable 'channel_list'
channel_list=requests.get(url)

# Extract the response: text
text=channel_list.text
#print(text)
# If we print whole code, might take time and memory so just take some part to check.
print(channel_list.text[:500])

#Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(text)
type(soup)
print(soup)
# Prettify the BeautifulSoup object: pretty_soup
pretty_soup=soup.prettify()
print(type(pretty_soup))
print(pretty_soup[:500])


#Parse response.text by creating a BeautifulSoup object, and assign this object to html_soup. 
#The 'html.parser' argument indicates that we want to do the parsing using Python’s built-in HTML parser.

#Now let's use the find_all() method 
#to extract all the div containers that have a class attribute of lister-item mode-advanced:

channel_containers =soup.find_all('div', class_ ="card pack-details")

print(channel_containers[0])
channel_details=channel_containers[2]
channel_details
print(channel_details.div.h2.text)

channel_priceconatainer = soup.find('span',class_="price-sm")
channel_priceconatainer
#channel_priceconatainer.text
#type(channel_priceconatainer)
#asd=channel_priceconatainer.text
#asda=float(asd)
#type(asda)
#type(asd)

#print(channel_priceconatainer[2])


#to solve by removing floats from span text
#eg 
'''for m in channel_price:
    if m ==' ₹ 0 / month':
        print('yes')'''
# Lists to store the scraped data in
channel_lists=[]
channel_price=[]

# Extract data from individual movie container

for i in channel_containers:
    #print(i)
    
    a=i.div.h2.text
    channel_lists.append(a)
    zxc=[]
    b=i.span.text
    c=re.findall(r"[-+]?\d*\.\d+|\d+", b)
    
 # since c is list + string value and not no. , convert to float  , but dataframe will be float bydefault.
    d=float(c[0])
    if d==float and d!=0.0:
        pass
    elif d==0.0:
        d=0
    channel_price.append(d)

 
    
print(channel_lists[10:20])
(print(channel_price))
## converting data to dataframe##

test_sets = pd.DataFrame({'channels':channel_lists,'price':channel_price})
print(test_sets.info())

test_sets.head()

+++++++++Till here one part of project is done to webscrap one set of data channels++++++++++
#here second part of collecting data of packs and assigning channels to it







