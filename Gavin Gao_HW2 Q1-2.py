#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Gavin Gao HW2 B9122


# In[ ]:


## Question 1 - 2


# In[1]:


from bs4 import BeautifulSoup
import urllib.request

seed_url = "https://www.sec.gov/news/pressreleases"

urls = [seed_url]    
seen = [seed_url]    
opened = []          
maxNumUrl = 10
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
    if "charges" in doc:
        count.append(curr_url)

    for tag in soup.find_all('a', href = True): 
        childUrl = tag['href'] 
        o_childurl = childUrl
        childUrl = urllib.parse.urljoin(seed_url, childUrl)
        if "https://www.sec.gov/news/press-release" in childUrl and childUrl not in seen:
            urls.append(childUrl)
            seen.append(childUrl)
            
        else:
            pass

for url in count:
    print(url)

