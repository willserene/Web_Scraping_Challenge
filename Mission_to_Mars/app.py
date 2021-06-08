from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Activate flask and mongoDB
app=Flask(__name__)
app.config["MONGO_URI"] ="mongodb://localhost:27017/mars_db_one"
mongo=PyMongo(app)



# Create index route
@app.route("/")
def index():
    mars_scrape=mongo.db.mars_data.find_one()
    return render_template("index.html", mars_data=mars_scrape)

@app.route("/scrape")

def scrape():
    scrape_data=sms.scrape()
    mongo.db.mars_data.update_many({},{'$set':scrape_data},True)
    return redirect("/",code=302)

if __name__ == "__main__":
    app.run(debug=True)
