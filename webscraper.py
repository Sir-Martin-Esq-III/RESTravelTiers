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

#Goes through table data to seperate the countries and adds them to a list
def retCountries(countries):
    countriesList=[]
    tableBody=countries.find('tbody')

    for row in tableBody:
        countriesRow=row.find('th')
        if countriesRow!=-1:
            #Could be replaced regex but not quite sure how to do it
            country=str(countriesRow).replace('<th scope="row">','').split('<')[0]
            countriesList.append(country)
    return countriesList

colors=[]
#Gets webpage and parses the HTMl
url="https://www.gov.uk/guidance/red-amber-and-green-list-rules-for-entering-england"
page=urlopen(url)
html_bytes =page.read()
html=html_bytes.decode("utf-8")
soup = BeautifulSoup(html,"html.parser")
#Seperates the 3 tables to its actual colors
red,amber,green =soup.find_all("table")
#adds all the colors in to a list so i can itr though them
colors.extend((red,amber,green))
for color in colors:
    #Could be replaced regex but not quite sure how to do it
    ColorValue=(str(color.find('th')).replace('<th scope="col">','').split('<')[0]).split(" ")[0]
    print(ColorValue,'\t')
    print(retCountries(color),'\n')
    #Convert the lists in to valid JSON format (when I decide how to format the API)



