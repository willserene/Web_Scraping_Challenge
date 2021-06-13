# web-scraping-challenge

This multi-step challenge required a web application be built to scrape various websites for data related to the Mission to Mars and display the information in a single HTML page.

The initial scraping was done using Jupyter Notebooks, BeautifulSoup, Pandas, and Requests/Splinter with the following information collected:
   - The latest News Title and Paragraph Text ([NASA Mars News Site](https://mars.nasa.gov/news/)
   - The latest Featured Space Image URL [here](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html)
   - A Table containing Mars Facts [here](https://space-facts.com/mars/)
   - The Name and High Res Image for Each of the Four Hemispheres [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

The second major step utilized MongoDB with Flask templating to create the HTML page that displays all the scraped information from above. 
    The jupyter notebook was converted into a Python script called mars_scrape.py. Executing this scrapes the above info and returns it all in a single dictionary. This was accomplished via a route ("/scrape") that imports the script and calls the appropriate function, as well as a route ("/") that queries the Mongo database and passes the mars data into an HTML template to display the data.
