from flask import Flask
app = Flask(__name__)


# Init selenium for getting videos
from selenium import webdriver
import time

browser = webdriver.PhantomJS()

browser.get("https://kissanime.to/")

while browser.title == "Please wait 5 seconds...":
    time.sleep(.1)


import animenowapi.views
