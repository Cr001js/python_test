# Required modules:)
import requests
from bs4 import BeautifulSoup
import arabic_reshaper
from bidi.algorithm import get_display
import re

# url here
r = requests.get('https://divar.ir/s/tehran/vehicles')

# print(r) (for show response)

# It's time to beautify XD
soup = BeautifulSoup(r.text, 'html.parser')
# finding cars :)
agahi_ha = soup.find_all(class_= 'post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46')

# Classification cars :)
title = []
for agahi in agahi_ha:
    title.append(agahi)

    
# finding cars with agreed price :)
list = []
for i in title:
    text = i.text
    ar = arabic_reshaper.reshape(text)
    ar2 = get_display(ar)
    if 'ﯿﻘﻓﺍﻮﺗ' in ar2:
            list.append(ar2)

# ok now we have cars with agreed price in our list
# time to sort them, and show them
for i in list:
    print(i)