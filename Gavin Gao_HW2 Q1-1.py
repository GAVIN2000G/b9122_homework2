#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Gavin Gao HW2 B9122


# In[ ]:


## Question 1 - 1


# In[1]:


from bs4 import BeautifulSoup
import urllib.request

seed_url = "https://www.federalreserve.gov/newsevents/pressreleases.htm"

urls = [seed_url]    
seen = [seed_url]    
opened = []          
maxNumUrl = 20
count = []
    
print("Starting with url="+str(urls))
while len(urls) > 0 and len(count) < maxNumUrl:
    try:
        curr_url=urls.pop(0)
        req = urllib.request.Request(curr_url,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()
        opened.append(curr_url)

    except Exception as ex:
        print("Unable to access= "+curr_url)
        print(ex)
        continue    

    soup = BeautifulSoup(webpage)  
    doc = soup.get_text().lower()
    if "covid" in doc:
        count.append(curr_url)

    for tag in soup.find_all('a', href = True): 
        childUrl = tag['href'] 
        o_childurl = childUrl
        childUrl = urllib.parse.urljoin(seed_url, childUrl)
        if "https://www.federalreserve.gov/newsevents/pressreleases/" in childUrl and childUrl not in seen:
            #print("***urls.append and seen.append***")
            urls.append(childUrl)
            seen.append(childUrl)
            
        else:
            #print("######")
            pass

for url in count:
    print(url)

