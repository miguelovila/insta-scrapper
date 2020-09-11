from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import common.terminal_messages as Msgs
import loggedin_user.methods as LoggedUserMethods
import loggedin_user.data as LoggedUserData
import json

class Driver:

    def __init__(self, headless):
        try:
            __options = Options()
            __options.headless = headless
            __options.set_preference('devtools.jsonview.enabled', False)
            self.__driver = webdriver.Firefox(firefox_options=__options, executable_path='./driver/geckodriver')
        except:
            print(Msgs.UNKNOWN_ERROR)

    def __del__(self):
        try:
            self.__driver.quit()
        except:
            print(Msgs.UNKNOWN_ERROR)

    def auth(self, args=[]):
        try:
            if (len(args) < 2) or (len(args) > 2):
                print(Msgs.INVALID_ARGS)
                return 
            self.deauth()       
            try:
                WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'username'))).send_keys(args[0])
                WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'password'))).send_keys(args[1])
                WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.L3NKy'))).click()
                WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.XTCLo')))
            except:
                print(Msgs.INVALID_CARDENTIALS)
            else:
                self.__get_logged_user_data()
        except:
            print(Msgs.UNKNOWN_ERROR)

    def deauth(self, args=[]):
        try:
            if (len(args) > 0):
                print(Msgs.INVALID_ARGS)
                return 
            self.__driver.get('https://instagram.com/accounts/logout')
            WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        except:
            print(Msgs.UNKNOWN_ERROR)

    def __get_logged_user_data(self):
        try:
            self.__driver.get('https://www.instagram.com/accounts/edit/?__a=1')
            __username = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)['form_data']['username']     
            
            self.__driver.get('https://www.instagram.com/' + __username + '/?__a=1')
            __response = WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text
            LoggedUserMethods.store_logged_user_data(__response)
            print(LoggedUserData.full_name)
        except:
            print(Msgs.UNKNOWN_ERROR)

    