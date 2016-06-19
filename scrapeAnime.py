from selenium import webdriver
import time


def main():

    # Start Selenium webdriver with PhantomJS
    browser = webdriver.PhantomJS()
    browser.set_window_size(1920, 1080)

    browser.get("https://kissanime.to/AdvanceSearch")

    # Wait for CloudFlare to finish
    while (browser.title == "Please wait 5 seconds..."):
        time.sleep(.25)

    print(browser.title)


if __name__ == "__main__":
    main()
