import os
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# mongo = PyMongo(app)

# Mongo connection set inline
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# set route to render index.html template using data from Mongo
@app.route("/")
def index():
    
    mars_data = mongo.db.data.find_one()
    return render_template("index.html", mars_data=mars_data)


# set route to trigger scrape function
@app.route("/scrape")
def scraper():
    # mars = mongo.db.mars
    
    
    scrape_data = mars_scrape.scrape()

    mars_data = mongo.db.data    

    # update the Mongo database
    mars_data.update({}, scrape_data, upsert=True)
    
       
    # redirect back to home page
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(debug=True)
