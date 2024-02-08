import sys
import json
from time import sleep
import config
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from playsound import playsound

if __name__ == "__main__":
    # initialize Selenium
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    # open URL
    driver.get(config.URL)

    # click dropdown "Privatkunde" to choose a "Dienstleistung"
    dropdown = driver.find_element(by=By.ID, value="category_7eb2f94a-d429-4fc5-9016-a7b503f2d3a4")
    dropdown.click()

    # increase "Zulassung" by +1
    increase_btn = driver.find_element(by=By.XPATH, value="//*[@id=\"category_content_7eb2f94a-d429-4fc5-9016-a7b503f2d3a4\"]/div[6]/div/div[2]/span[3]")
    increase_btn.click()

    # click "Weiter" button
    next_btn = driver.find_element(by=By.ID, value="forward-service")
    next_btn.click()

    locations = {
        #"5013ee70-5ae3-4078-891d-8ca0cd600a2a": "Böblingen",
        #"e3b1e44c-0c3d-4bfa-8197-a44f69f0bc38": "Herrenberg",
        "c88d01a2-24c8-4c1c-8e99-eac41cc94b51": "Leonberg"
    }

    # iterate over all locations until we find something
    while True:
        for location in locations:
            # click button for given location
            print(f"{datetime.now()} Checking {locations[location]}...")
            location_btn = driver.find_element(by=By.ID, value=location)
            location_btn.click()

            # click "Weiter" button
            next_btn = driver.find_element(by=By.ID, value="location_next")
            next_btn.click()

            # check if appointments are available
            content = driver.find_element(by=By.ID, value="appointment_holder")
            if "aktuell sind alle verfügbaren Termine ausgebucht" in content.text:
                print(f"{datetime.now()} Nothing found in {locations[location]}!")
                sleep(config.SLEEP)
                # go back to location overview page
                back_btn = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/form/div[3]/div[5]/div/div[2]/button")
                back_btn.click()
                sleep(config.SLEEP)
            else:
                print(f"{datetime.now()} Found something in {locations[location]}!")
                playsound(config.ALARM)
                sys.exit(0)
