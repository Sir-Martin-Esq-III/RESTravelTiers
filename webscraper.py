'''
What this program does
    It scrapes the UK govt website which is updated by them and fetches the tables relating to the 3
    tiers "red" "amber" and "green" and creates JSON files which can be used by anyone who requests them

What still needs doing
    Finish designing the API format
        format the lists in to the correct JSON notation
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

#Goes through table data to seperate the countries and adds them to a list
def retCountries(countries):
    countriesList=[]
    tableBody=countries.find('tbody')
    for row in tableBody:
        val=re.findall(">(.*)<",str(row.find('th')))
        #Empty lists would actually be (soon to be) updates to the list
        if len(val)>0:
            countriesList.append(val)    
    return countriesList

#Gets webpage and parses the HTMl
url="https://www.gov.uk/guidance/red-amber-and-green-list-rules-for-entering-england"
page=urlopen(url)
html =page.read().decode("utf-8")
soup = BeautifulSoup(html,"html.parser")

#Seperates the 3 tables to its actual colors
red,amber,green =soup.find_all("table")
#adds all the colors in to a list so i can itr though them
colors= [red,amber,green]   

for color in colors:
    ColorValue=str(re.findall(">(.*)<",str(color.find('th')))[0]).split()[0]
    print(ColorValue,'\t')
    print(retCountries(color),'\n')
    #Convert the lists in to valid JSON format (when I decide how to format the API)



