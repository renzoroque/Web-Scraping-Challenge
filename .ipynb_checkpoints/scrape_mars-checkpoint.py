# Declare Dependencies 
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import pymongo
import os
import time
import requests
import warnings
warnings.filterwarnings('ignore')

def init_browser():
    # @NOTE: Path to my chromedriver
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)


# NASA MARS NEWS
def scrape_mars_news():

        # Initialize browser 
        browser = init_browser()
        
        #Create Mars dictionary
        # mars_info = {}

        # Visit Nasa news url through splinter module
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)

        # HTML Object
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = bs(html, 'html.parser')

        # Retrieve the latest element that contains news title and   news_paragraph
        article = soup.find("div", class_='list_text')
        news_title = article.find('div', class_='content_title').text
        news_p = article.find('div', class_='article_teaser_body').text

        # Dictionary entry from MARS NEWS
        # mars_info["News Title"] = news_title
        # mars_info["News Article"] = news_p

        return mars_info

        browser.quit()

# FEATURED IMAGE
def scrape_mars_image():

        # Initialize browser 
        browser = init_browser()

        #browser.is_element_present_by_css("img.jpg", wait_time=1)

        # Visit Mars Space Images through splinter module
        featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(featured_image_url)# Visit Mars Space Images through splinter module

        browser.click_link_by_partial_text('FULL IMAGE')
        time.sleep(5)

        # HTML Object 
        html_image = browser.html

        # Parse HTML with Beautiful Soup
        image_soup = bs(html_image, 'html.parser')

        # Retrieve background-image url from style tag 
        feat_img_url  = featured_image_url + image_soup.find(('figure', class_=='lede').a['href']

        # Dictionary entry from FEATURED IMAGE
        # mars_info["Featured Image"] = feat_img_url 
        
        # return mars_info

        # browser_quit()

        
# Mars Facts
def scrape_mars_facts():

        mars_facts_url = 'https://space-facts.com/mars/'

        table = pd.read_html(mars_facts_url)
        mars_facts = table[1]
        mars_facts = mars_facts.drop(["Earth"],axis = 1)
        mars_facts.columns = ["Description", "Value"]
        mars_facts.set_index("Description", inplace=True)
        mars_facts

        mars_facts.to_html('table.html')

        # mars_info["Mars Table"] = mars_facts

        return mars_info

# Mars Hemisphere

def scrape_mars_hemispheres():

        hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find("div", class_ = "result-list" )
    hemispheres = results.find_all("div", class_="item")

#Create empty dictionary to store the urls:
    hemisphere_image_urls = []

for hemisphere in hemispheres:
    title = hemisphere.find('h3').text
    image_link = hemisphere.find("a")["href"]
    image_url = "https://astrogeology.usgs.gov" + image_link
    browser.visit(image_url)
    html = browser.html
    soup = bs(html, "html.parser")
    image_download = soup.find("div", class_ = "downloads")
    final_image = image_download.find("a")["href"]
    hemisphere_image_urls.append({"Title": title, "Img_url": final_image})

        # mars_info["Hemisphere Images"] = final_image
        

    mars_info = {
        'News Title' = news_title,
        'News Article' = news_p,
        'Featured Image' = feat_img_url,
        'Mars Table' = mars_facts,
        'Hemisphere Images' = final_image
        }
       
        browser.quit()

        # Return mars_data dictionary 

        return mars_info