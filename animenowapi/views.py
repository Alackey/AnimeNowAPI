from animenowapi import app, db
from flask import request, jsonify
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


# Get anime matching query
@app.route("/search")
def search():
    if request.method == "GET":

        # Get anime that contain a keyword or match the given title
        animes_found = db.search(query=request.args.get("query"))

        # Aggregate titles from animes found in database
        titles = []
        for anime in animes_found:
            titles.append(anime["title"])

        return jsonify({"titles": titles})


# Get the url of an anime
@app.route("/videourl")
def videourl():
    if request.method == "GET":

        # Get the anime information
        anime = db.search(
            query=request.args.get("query"),
            is_title=True
        )

        # If not anime is found
        if anime is None:
            return jsonify({"url": "Error: Title not found", "Error": True})


        browser = webdriver.PhantomJS()

        browser.get(anime["url"])

        while browser.title == "Please wait 5 seconds...":
            time.sleep(.1)

        print("Page Title:", browser.title)

        ### Test grabbing episodes
        soup = BeautifulSoup(browser.page_source, "html.parser")
        episodes = soup.select("td > a")
        if 1 < len(episodes) and len(episodes) < 50:
            for ep in episodes:
                # print(ep.string.strip())
                print("Href: {}", ep["href"])

        return jsonify({"url": anime["url"]})
