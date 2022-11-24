from Scraper import HomePage, PharmacyPage
from Driver import WebDriver

from time import sleep

driver = WebDriver()

home = HomePage(driver)

sleep(30)

home.submit_button()