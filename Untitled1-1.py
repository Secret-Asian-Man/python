//called scraping (for data)

# coding: utf-8

# In[38]:

import requests
from bs4 import BeautifulSoup

home_url = "htpp://www.nba.com"
teams_url = "http://www.nba.com/teams"
teams_html = requests.get(teams_url)


# In[39]:

souped_teams = BeautifulSoup(teams_html.text)


# In[40]:

list_of_links = souped_teams.find_all("a")


# In[41]:

type(list_of_links[9].get("href"))


# In[42]:

stats_links = []
for tag in list_of_links:
    if tag.get("href") and "/stats/" in tag.get("href"):
        stats_links.append(home_url + tag.get("href"))

print(stats_links)


# In[43]:

#stats_links = [tag.get("href") for tag in list_of_links if (tag.get("href") and "stats" in tag.get("href"))]
#print(stats_links)


# In[44]:

first = list_of_links[1]
type(first)


# In[45]:

first.string


# In[ ]:






.json is a common form of expressing api

PLOTTING (matplotlib.org)
import matplotlib.pyplot as plt //so now instead of typing "matplotlib.pyplot" everytime i can type "plt"
plt.plot([4,2,7,10], [1,2,3,4], 'ro') //[x's][y's]
plt.ylabel("Some stuff")
plt.show();

