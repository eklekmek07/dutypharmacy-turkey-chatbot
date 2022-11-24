from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

 
class WebDriver():
    def __init__(self):
        self.driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def close(self):
        self.driver.close()
        self.driver.quit()