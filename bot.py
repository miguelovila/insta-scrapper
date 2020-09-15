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
                self.set_logged_user_basic_data()
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

    def set_logged_user_basic_data(self):
        try:
            self.__driver.get('https://www.instagram.com/accounts/edit/?__a=1')        
            self.__driver.get('https://www.instagram.com/' + json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)['form_data']['username'] + '/?__a=1')
            LoggedUserMethods.set_logged_user_basic_data(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
        except Exception as e:
            Msgs.print_error(e)

    def set_logged_user_followers(self, limit = '0'):
        if (LoggedUserData.id == ''):
            print(Msgs.LOGIN_REQUIRED)
            return
        if not(limit.isnumeric()):
            print(Msgs.INVALID_ARGS)
            return
        end_cursor = ''
        next_page = True
        limit_reached = False
        limit = int(limit)
        LoggedUserData.followers_list.clear()
        count = 0
        try:
            while next_page and not(limit_reached):
                self.__driver.get('https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"' + LoggedUserData.id + '","first":50,"after":"' + end_cursor + '"}')
                response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
                for i in range(len(response['data']['user']['edge_followed_by']['edges'])):
                    follower = (response['data']['user']['edge_followed_by']['edges'][i]['node']['full_name'],response['data']['user']['edge_followed_by']['edges'][i]['node']['username'],response['data']['user']['edge_followed_by']['edges'][i]['node']['id'])
                    LoggedUserData.followers_list.append(follower)
                    count += 1
                    if (limit != '0'):
                        if (count == limit):
                            limit_reached = True
                            break            
                next_page = response['data']['user']['edge_followed_by']['page_info']['has_next_page']
                end_cursor = str(response['data']['user']['edge_followed_by']['page_info']['end_cursor'])
            LoggedUserMethods.get_logged_user_followers_list()
        except Exception as e:
            Msgs.print_error(e)

    def set_logged_user_following(self, limit = '0'):
        if (LoggedUserData.id == ''):
            print(Msgs.LOGIN_REQUIRED)
            return
        if not(limit.isnumeric()):
            print(Msgs.INVALID_ARGS)
            return
        end_cursor = ''
        next_page = True
        limit_reached = False
        limit = int(limit)
        LoggedUserData.following_list.clear()
        count = 0
        try:
            while next_page and not(limit_reached):
                self.__driver.get('https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={"id":"' + LoggedUserData.id + '","first":50,"after":"' + end_cursor + '"}')
                response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
                for i in range(len(response['data']['user']['edge_follow']['edges'])):
                    followee = (response['data']['user']['edge_follow']['edges'][i]['node']['full_name'],response['data']['user']['edge_follow']['edges'][i]['node']['username'],response['data']['user']['edge_follow']['edges'][i]['node']['id'])
                    LoggedUserData.following_list.append(followee)
                    count += 1
                    if (limit != '0'):
                        if (count == limit):
                            limit_reached = True
                            break            
                next_page = response['data']['user']['edge_follow']['page_info']['has_next_page']
                end_cursor = str(response['data']['user']['edge_follow']['page_info']['end_cursor'])
            LoggedUserMethods.get_logged_user_following_list()
        except Exception as e:
            Msgs.print_error(e)

    def set_logged_user_posts(self, limit = '0'):
        if (LoggedUserData.id == ''):
            print(Msgs.LOGIN_REQUIRED)
            return
        if not(limit.isnumeric()):
            print(Msgs.INVALID_ARGS)
            return
        end_cursor = ''
        next_page = True
        limit_reached = False
        limit = int(limit)
        LoggedUserData.posts_list.clear()
        count = 0
        try:
            while next_page and not(limit_reached):
                self.__driver.get('https://www.instagram.com/graphql/query/?query_hash=bfa387b2992c3a52dcbe447467b4b771&variables={"id":"' + LoggedUserData.id + '","first":50,"after":"' + end_cursor + '"}')
                response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
                for i in range(len(response['data']['user']['edge_owner_to_timeline_media']['edges'])):
                    post = (response['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['__typename'],response['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['id'],response['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['shortcode'])
                    LoggedUserData.posts_list.append(post)
                    count += 1
                    if (limit != '0'):
                        if (count == limit):
                            limit_reached = True
                            break            
                next_page = response['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
                end_cursor = str(response['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor'])
            LoggedUserMethods.get_logged_user_posts_list()
        except Exception as e:
            Msgs.print_error(e)