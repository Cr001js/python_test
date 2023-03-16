import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://github.com/Cr001js/python_test')

soup = BeautifulSoup(r.text, 'html.parser')

folders_name = soup.find_all(class_ = 'Details-content--hidden-not-important js-navigation-container js-active-navigation-container d-md-block')[-1].extract()

# f = soup.find_all(class_ = 'flex-auto min-width-0 col-md-2 mr-3')[-1].extract()

t = str(folders_name)


name = re.findall('/tree\/master\/(.*)', t)

names = []

for i in name:
    names.append(re.findall('">(.*?)<', i))

# print(t)

Update = re.findall('href="\/Cr001js\/python_test\/commit\/(.*)<', t)

Updates = []

for i in Update:
    v = re.findall('title=".*">(.*)', i)
    Updates.append(v)

Update_datetime = re.findall('tense="past">(.*)<', t)