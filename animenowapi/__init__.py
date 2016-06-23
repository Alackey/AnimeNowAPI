from flask import Flask
app = Flask(__name__)


# Init selenium for getting videos
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.PhantomJS()

browser.get("https://kissanime.to/")

while browser.title == "Please wait 5 seconds...":
    time.sleep(.1)


import animenowapi.views
