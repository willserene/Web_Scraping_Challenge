# Import Splinter, BeautifulSoup, and Pandas
import os
import pandas as pd
import datetime as dt
import time
from splinter import Browser, browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    
    data_dict = {}
    
    # Initiate headless driver for deployment
    # browser = Browser("chrome", executable_path="chromedriver", headless=True)
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # news_title, news_p = mars_news(browser)
    
    # Run all scraping functions and store results in a dictionary
    data_dict["news_title"] = mars_news(browser)["news_title"]
    data_dict["news_p"] = mars_news(browser)["news_p"]
    data_dict["featured_image_url"] = featured_image(browser)
    data_dict["mars_facts_table"] = mars_facts(browser)
    data_dict["hemispheres"] = scrape_hemispheres(browser)
    
    
    browser.quit()

    return data_dict
   

def mars_news(browser):
    
    mars_news_dict = {}
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    time.sleep(2)
   
   # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    news_soup = bs(html, "html.parser")

    # News
    news_section = news_soup.find_all('div', class_="list_text")[0]
    # News title 
    news_title = news_section.find(class_="content_title").text
    mars_news_dict["news_title"] = news_title
    # News paragraph
    news_p = news_section.find(class_="article_teaser_body").text
    mars_news_dict["news_p"] = news_p
    
    return mars_news_dict
    
 
def featured_image(browser):
    
    img_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(img_url)
    time.sleep(2)
       
    html = browser.html
    img_soup = bs(html, "html.parser")

    mars_image = img_soup.find('img', class_ = "headerimage")['src']
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space' + '/' + mars_image

    return featured_image_url

def mars_facts(browser):
    facts_url = 'https://space-facts.com/mars/'

    table = pd.read_html(facts_url)
    facts_table = pd.DataFrame(table[0])
    facts_table.columns = ['Description', 'Value']                  
    
    
    facts_table_html = facts_table.to_html(classes = "table table-striped")
        
    return facts_table_html

def scrape_hemispheres(browser):

    hemispheres = []
    
    mars_hemispheres_url = 'https://marshemispheres.com/'

    hem_dict = {}

    browser.visit(mars_hemispheres_url)
    time.sleep(2)
    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    hemisphere_title1 = soup.find('h2', class_ = 'title').text
    hemisphere_image1 = soup.find('img', class_ = 'wide-image')['src']
    hemisphere_image1_url = f'{mars_hemispheres_url}{hemisphere_image1}'
    hem_dict["title1"] = hemisphere_title1
    hem_dict["url1"] = hemisphere_image1_url
    
  
    browser.visit(mars_hemispheres_url)
    time.sleep(2)
    browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    hemisphere_title2 = soup.find('h2', class_ = 'title').text
    hemisphere_image2 = soup.find('img', class_ = 'wide-image')['src']
    hemisphere_image2_url = f'{mars_hemispheres_url}{hemisphere_image2}'
    hem_dict["title2"] = hemisphere_title2
    hem_dict["url2"] = hemisphere_image2_url
    

    browser.visit(mars_hemispheres_url)
    time.sleep(2)
    browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    hemisphere_title3 = soup.find('h2', class_ = 'title').text
    hemisphere_image3 = soup.find('img', class_ = 'wide-image')['src']
    hemisphere_image3_url = f'{mars_hemispheres_url}{hemisphere_image3}'
    hem_dict["title3"] = hemisphere_title3
    hem_dict["url3"] = hemisphere_image3_url
    

    browser.visit(mars_hemispheres_url)
    time.sleep(2)
    browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()
    html = browser.html
    soup = bs(html, 'html.parser')
    hemisphere_title4 = soup.find('h2', class_ = 'title').text
    hemisphere_image4 = soup.find('img', class_ = 'wide-image')['src']
    hemisphere_image4_url = f'{mars_hemispheres_url}{hemisphere_image4}'
    hem_dict["title4"] = hemisphere_title4
    hem_dict["url4"] = hemisphere_image4_url
   
    hemispheres.append(hem_dict)

    return hemispheres


if __name__ == "__main__":

    print(scrape())
