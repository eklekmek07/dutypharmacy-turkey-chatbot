from Driver import WebDriver
from selenium.webdriver.common.by import By

class Page:
    def __init__(self) -> None:
        pass

    def find_element_with_locators(self):
        #use locators dict to soften this up go honey
        pass


class HomePage:
    def __init__(self, driver):
        self.driver = driver.driver
        self.open()

    def open(self):
        self.driver.get("https://www.turkiye.gov.tr/saglik-titck-nobetci-eczane-sorgulama")

    locators = {
        "Submit": (By.XPATH, "//input[@value='Sorgula']"),
        "Select_Date": (By.ID, "nobetTarihi")
        }

    def submit_button(self):
        self.driver.find_element(By.XPATH, "//input[@value='Sorgula']")

class PharmacyPage:
    locators = {}

