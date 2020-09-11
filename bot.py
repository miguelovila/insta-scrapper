from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class Driver:

    def __init__(self, headless):
        __options = Options()
        __options.headless = headless
        __options.set_preference('devtools.jsonview.enabled', False)
        self.__driver = webdriver.Firefox(firefox_options=__options, executable_path='./driver/geckodriver')

    def __del__(self):
        self.__driver.quit()