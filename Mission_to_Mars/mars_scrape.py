# Import Splinter, BeautifulSoup, and Pandas
import os
import pandas as pd
import datetime as dt
import time
from splinter import Browser, browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Initiate headless driver for deployment
    # browser = Browser("chrome", executable_path="chromedriver", headless=True)
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)
    
    news_title, news_p = mars_news(browser)
    
    # Run all scraping functions and store results in a dictionary
    data = {
        "News Title": news_title,
        "News Paragraph": news_p,
        "Featured Image": featured_image(browser),
        "Mars Facts": mars_facts(),
        "Hemispheres": hemispheres(browser),
        "last_modified": dt.datetime.now()
        }
        
    browser.quit()

    return data
   

def mars_news(browser):
    
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
    # News paragraph
    news_p = news_section.find(class_="article_teaser_body").text
    
    return news_title, news_p
 
def featured_image(browser):
    
    img_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(img_url)
    time.sleep(2)
       
    html = browser.html
    img_soup = bs(html, "html.parser")

    mars_image = img_soup.find('img', class_ = "headerimage")['src']
    featured_image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space' + '/' + mars_image

    return featured_image_url

def mars_facts():
    facts_url = 'https://space-facts.com/mars/'

    table = pd.read_html(facts_url)
    facts_table = pd.DataFrame(table[0])
    facts_table.columns = ['Description', 'Mars']                  
    # facts_table.set_index('Description', inplace = True)
    
    facts_table_html = facts_table.to_html(classes = "table table-striped")
        
    return facts_table_html

def hemispheres(browser):

    mars_hemispheres_url = 'https://marshemispheres.com/'

    browser.visit(mars_hemispheres_url)
    time.sleep(2)
    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()

    html = browser.html
    soup = bs(html, 'html.parser')

    hemisphere_title1 = soup.find('h2', class_ = 'title').text
    hemisphere_image1 = soup.find('img', class_ = 'wide-image')['src']
    hemisphere_image1_url = f'{mars_hemispheres_url}{hemisphere_image1}'
  
    browser.visit(mars_hemispheres_url)
    time.sleep(2)
    browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()

    html = browser.html
    soup = bs(html, 'html.parser')

    hemisphere_title2 = soup.find('h2', class_ = 'title').text
    hemisphere_image2 = soup.find('img', class_ = 'wide-image')['src']
    hemisphere_image2_url = f'{mars_hemispheres_url}{hemisphere_image2}'

    browser.visit(mars_hemispheres_url)
    time.sleep(2)
    browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()

    html = browser.html
    soup = bs(html, 'html.parser')

    hemisphere_title3 = soup.find('h2', class_ = 'title').text
    hemisphere_image3 = soup.find('img', class_ = 'wide-image')['src']
    hemisphere_image3_url = f'{mars_hemispheres_url}{hemisphere_image3}'

    browser.visit(mars_hemispheres_url)
    time.sleep(2)
    browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()

    html = browser.html
    soup = bs(html, 'html.parser')

    hemisphere_title4 = soup.find('h2', class_ = 'title').text
    hemisphere_image4 = soup.find('img', class_ = 'wide-image')['src']
    hemisphere_image4_url = f'{mars_hemispheres_url}{hemisphere_image4}'

    hemisphere_image_urls = {
        "Hemisphere1": hemisphere_title1, "Image1": hemisphere_image1_url,
        "Hemisphere2": hemisphere_title2, "Image2": hemisphere_image2_url,
        "Hemisphere3": hemisphere_title3, "Image3": hemisphere_image3_url,
        "Hemisphere4": hemisphere_title4, "Image4": hemisphere_image4_url}
    

    return hemisphere_image_urls



if __name__ == "__main__":

    print(scrape())
