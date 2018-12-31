
# coding: utf-8

# In[8]:


#import dependencies
from splinter import Browser
from bs4 import BeautifulSoup


# In[13]:


#setup path
executable_path = {'executable_path': '/Users/ellen/Downloads/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[14]:


#path to mars data/site to scrape
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

#delay loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# ### NASA Mars News

# In[15]:


#use html on NASA page - change to BeautifulSoup

html = browser.html
news_soup = BeautifulSoup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[16]:


slide_elem.find("div", class_='content_title')


# In[17]:


# Save first tag as `news_title` - keep track of variable 'news_title'
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[19]:


#Repeat for paragraph text news_p
news_p= slide_elem.find("div", class_="article_teaser_body").get_text()
news_p


# ### JPL Mars Space Images - Featured Image

# In[25]:


#designate new URL for JPL image
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[26]:


#find image (featured image at top of page) full image icon
# Use inspect + find 'full_image' button and click action

full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[27]:


# repeat for 'more info' button to get element info

browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.find_link_by_partial_text('more info')
more_info_elem.click()


# In[28]:


# parse with Beautiful Soup

html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[29]:


# get image src info for url

img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[31]:


# name and display variable for url 

featured_image_url= f'https://www.jpl.nasa.gov{img_url_rel}'
featured_image_url


# ### Mars Weather

# In[32]:


# designate new url for mars weather

url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(url)


# In[33]:


# Parse with Beautiful Soup

html = browser.html
weather_soup = BeautifulSoup(html, 'html.parser')


# In[34]:


# find tweet

mars_weather_tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})


# In[35]:


# use paragraph element to get text

mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()
mars_weather


# ### Mars Facts

# In[37]:


# import depdency for pandas
import pandas as pd


# In[42]:


# Create DataFrame with Mars Facts info - rename column headers and reset index

df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['Category', 'Mars Info']
df.set_index('Category', inplace=True)
df


# In[43]:


# convert df to html table

df.to_html()


# ### Mars Hemispheres

# In[51]:


# set url
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[52]:


# Create empty array for image urls list
hemisphere_image_urls = []


# In[53]:


# List the hemispheres and assign to links variable - 
links = browser.find_by_css("a.product-item h3")


# In[54]:


# loop through links
# hemisphere empty dictionary created
# click each link
# get image url tag from css
# add to list and go back


for i in range(len(links)):
    hemisphere = {}
    browser.find_by_css("a.product-item h3")[i].click()
    sample_elem = browser.find_link_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']
    hemisphere['title'] = browser.find_by_css("h2.title").text
    hemisphere_image_urls.append(hemisphere)
    browser.back()


# In[56]:


hemisphere_image_urls

