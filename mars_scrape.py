# Import Splinter, BeautifulSoup, and Pandas
import os
import pandas as pd
import datetime as dt
from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    # Initiate headless driver for deployment
    # executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    news_title, news_p = mars_news(browser)
    featured_image_url = featured_image(browser)
    mars_facts_html = mars_facts()

    # Run all scraping functions and store results in a dictionary
    data = {
        "News Title": news_title,
        "News Paragraph": news_p,
        "Featured Image": featured_image_url,
        "Mars Facts": mars_facts_html,
        # "Hemispheres": hemispheres,
        "last_modified": dt.datetime.now()
        }
        
    browser.quit()

    return (data)

   

def mars_news(browser):
    # browser = start_browser()
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)

    # Optional delay for loading the page
    # browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Create BeautifulSoup object; parse with 'html.parser'
    # Scraping page into Soup
    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = bs(html, "html.parser")

    # News
    news_section = news_soup.find_all('div', class_="list_text")[0]

    # News title 
    news_title = news_section.find(class_="content_title").text

    # News paragraph
    news_p = news_section.find(class_="article_teaser_body").text
    # Scrape Mars News
    # Visit the mars nasa news site
    
    return news_title, news_p
 
def featured_image(browser):
     # browser = start_browser()
    img_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(img_url)

    # Optional delay for loading the page
    # browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Create BeautifulSoup object; parse with 'html.parser'
    # Scraping page into Soup
    # Convert the browser html to a soup object and then quit the browser
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
    facts_table.set_index('Description', inplace = True)
    
    facts_table_html = facts_table.to_html(classes = "table table-striped")
    # cleaning table
    # facts_table.replace('\n', '')
    
    return facts_table_html


# def hemispheres(browser):
#     # A way to break up long strings
#     url = (
#         "https://astrogeology.usgs.gov/search/"
#         "results?q=hemisphere+enhanced&k1=target&v1=Mars"
#     )

#     browser.visit(url)

#     # Click the link, find the sample anchor, return the href
#     hemisphere_image_urls = []
#     for i in range(4):
#         # Find the elements on each loop to avoid a stale element exception
#         browser.find_by_css("a.product-item h3")[i].click()
#         hemi_data = scrape_hemisphere(browser.html)
#         # Append hemisphere object to list
#         hemisphere_image_urls.append(hemi_data)
#         # Finally, we navigate backwards
#         browser.back()

#     return hemisphere_image_urls


# def scrape_hemisphere(html_text):
#     # parse html text
#     hemi_soup = soup(html_text, "html.parser")

#     # adding try/except for error handling
#     try:
#         title_elem = hemi_soup.find("h2", class_="title").get_text()
#         sample_elem = hemi_soup.find("a", text="Sample").get("href")

#     except AttributeError:
#         # Image error will return None, for better front-end handling
#         title_elem = None
#         sample_elem = None

#     hemispheres = {
#         "title": title_elem,
#         "img_url": sample_elem
#     }

#     return hemispheres


# if __name__ == "__main__":

    # If running as script, print scraped data
    
    
