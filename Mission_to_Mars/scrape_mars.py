from bs4 import BeautifulSoup
from splinter import Browser
import requests
from webdriver_manager.chrome import ChromeDriverManager
import time
import pymongo
from pymongo import MongoClient
mongo_conn=pymongo.MongoClient('mongodb://localhost:27017')
mars_db_one = mongo_conn["mars_db_one"]
mars_info = mars_db_one["mars"]
import pandas as pd