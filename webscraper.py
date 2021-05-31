'''
What this program does
    It scrapes the UK govt website which is updated by them and fetches the
    tables relating to the 3 tiers "red" "amber" and "green" and creates a 
    JSON file which can be used by anyone who requests them
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

#Goes through table data to seperate the countries and adds them to a list
def retCountries(countries,ColorValue,jsonDict):
    tableBody=countries.find('tbody')
    for row in tableBody:
        val=re.findall(">(.*)<",str(row.find('th')))
        try:                                            #Sometimes val[0]
            if len(val[0])>0:                           #Cannot be accessed
                jsonDict[val[0]]={"Tier":ColorValue}    #So we just pass these
        except:                                         #Instances
            pass

#Gets webpage and parses the HTMl
url=("https://www.gov.uk/guidance/red-amber-and-green-list-rules-for-entering-england")
page=urlopen(url)
html =page.read().decode("utf-8")
soup = BeautifulSoup(html,"html.parser")

finalJsonObject={}

#Seperates the 3 tables to its actual colors
red,amber,green =soup.find_all("table")
#adds all the colors in to a list so i can itr though them
colors= [red,amber,green]   

for color in colors:
    ColorValue=str(re.findall(">(.*)<",str(color.find('th')))[0]).split()[0]
    retCountries(color,ColorValue,finalJsonObject)

#Write to JSON file
with open('data.json','w') as File:
    json.dump(finalJsonObject,File)





