from animenowapi import app, browser, db
from flask import request, jsonify
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

        print(browser.title)
        # Open new window for selenium browser
        # body = browser.find_element_by_tag_name("body")
        # body.send_keys(Keys.CONTROL + 'n')
        open_window_script = 'return window.open("' + anime["url"] + '", "any", \
            "height = 450, width = 800, menubar=yes,scrollbars=yes, \
            toolbar=yes,location=no,resizable=yes");'
        handle = browser.execute_script(open_window_script)
        # WebDriverWait(browser, 10).until(
        #     EC.element_to_be_clickable((By.ID, "selectEpisode"))
        # )
        for handle in browser.window_handles:
            print(handle)
        browser.switch_to_window(browser.window_handles[-1])
        print(browser.title)

        return jsonify({"url": anime["url"]})
