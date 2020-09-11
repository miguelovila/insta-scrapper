from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import common.terminal_messages as Msgs

class Driver:

    def __init__(self, headless):
        __options = Options()
        __options.headless = headless
        __options.set_preference('devtools.jsonview.enabled', False)
        self.__driver = webdriver.Firefox(firefox_options=__options, executable_path='./driver/geckodriver')

    def __del__(self):
        self.__driver.quit()

    def auth(self, args=[]):
        if (len(args) < 2) or (len(args) > 2):
            print(Msgs.INVALID_ARGS)
            return 

        self.deauth()
        WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'username'))).send_keys(args[0])
        WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'password'))).send_keys(args[1])
        WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.L3NKy'))).click()

    def deauth(self, args=[]):
        if (len(args) > 0):
            print(Msgs.INVALID_ARGS)
            return 

        self.__driver.get('https://instagram.com/accounts/logout')
        WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))