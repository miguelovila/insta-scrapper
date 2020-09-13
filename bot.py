from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import common.terminal_messages as Msgs
import loggedin_user.methods as LoggedUserMethods
import json

class Driver:

    def __init__(self, headless):
            __options = Options()
            __options.headless = headless
            __options.set_preference('devtools.jsonview.enabled', False)
            self.__driver = webdriver.Firefox(firefox_options=__options, executable_path='./driver/geckodriver')

    def __del__(self):
        self.__driver.quit()

    def auth(self, args=[]):
        try:
            self.deauth()
            WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'username'))).send_keys(args[0])
            WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'password'))).send_keys(args[1])       
            try:
                WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.L3NKy'))).click()
                WebDriverWait(self.__driver, 5).until_not(expected_conditions.presence_of_element_located((By.NAME, 'username')))
                self.__set_logged_user_data()
            except:
                print(Msgs.INVALID_CARDENTIALS)          
        except Exception as e:
            Msgs.print_error(e)

    def deauth(self, args=[]):
        try:
            self.__driver.get('https://instagram.com/accounts/logout')
            WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
            LoggedUserMethods.del_logged_user_data()
        except Exception as e:
            Msgs.print_error(e)

    def __set_logged_user_data(self):
        try:
            self.__driver.get('https://www.instagram.com/accounts/edit/?__a=1')        
            self.__driver.get('https://www.instagram.com/' + json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)['form_data']['username'] + '/?__a=1')
            LoggedUserMethods.set_logged_user_data(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
        except Exception as e:
            Msgs.print_error(e)