from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import db_scraping
import time


def main():

    # Start Selenium webdriver with PhantomJS
    browser = webdriver.PhantomJS()
    browser.set_window_size(1920, 1080)

    browser.get("https://kissanime.to/AdvanceSearch")

    # Wait for CloudFlare to finish and button is clickable
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "btnSubmit"))
    )

    print("Navigated to search page. Title:", browser.title)

    # Search nothing to get all anime on one page
    search_btn = browser.find_element_by_id("btnSubmit")
    search_btn.click()

    # Get titles and links for all anime
    soup = BeautifulSoup(browser.page_source, "html.parser")
    anime_list = soup.select("td > a")

    print("Got all anime HTML")

    # Update anime list
    db_scraping.update_anime(anime_list)

    browser.close()


if __name__ == "__main__":
    main()
