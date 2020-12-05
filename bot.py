from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import common.terminal_messages as Msgs
import loggedin_user.methods as LoggedUserMethods
import loggedin_user.data as LoggedUserData
import selected_user.methods as SelectedUserMethods
import selected_user.data as SelectedUserData
import selected_post.data as SelectedPostData
import selected_post.methods as SelectedPostMethods
import json
import re

class Driver:

#region "DRIVER HANDLER"

    def __init__(self, headless):
            __options = Options()
            __options.headless = headless
            __options.set_preference('devtools.jsonview.enabled', False)
            __options.binary_location = "C:/firefox_binary/firefox.exe"
            self.__driver = webdriver.Firefox(firefox_options=__options, executable_path='./driver/geckodriver.exe')

    def __del__(self):
        self.__driver.quit()

#endregion

#region "LOGGED USER"

    def auth(self, args=[]):
        try:
            self.deauth()
            WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'username'))).send_keys(args[0])
            WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.NAME, 'password'))).send_keys(args[1])       
            try:
                WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.L3NKy'))).click()
                WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.XTCLo')))      
                id = re.search('viewerId":"(.*)"},"country_code":"', self.__driver.page_source)
                LoggedUserData.id = id.group(1)
                username = re.search('"username":"(.*)","badge_count":"', self.__driver.page_source)
                LoggedUserData.username = username.group(1)
                fullname = re.search('"full_name":"(.*)","has_phone_number"', self.__driver.page_source)
                LoggedUserData.full_name = fullname.group(1)
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

    def get_logged_user_basic_data(self):
        if (LoggedUserData.id == ''):
            print(Msgs.LOGIN_REQUIRED)
            return
        try:       
            self.__driver.get('https://www.instagram.com/' + LoggedUserData.username + '/?__a=1')
            LoggedUserMethods.set_logged_user_basic_data(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
        except Exception as e:
            Msgs.print_error(e)

    def get_logged_user_followers(self, limit = '0'):
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
        LoggedUserData.followers_search = True
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
        except Exception as e:
            Msgs.print_error(e)

    def get_logged_user_following(self, limit = '0'):
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
        LoggedUserData.following_search = True
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
        except Exception as e:
            Msgs.print_error(e)

    def get_logged_user_posts(self, limit = '0'):
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
        LoggedUserData.posts_search = True
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
        except Exception as e:
            Msgs.print_error(e)

#endregion

#region "SELECTED USER"

    def select_user(self, username):
        try:
            SelectedUserMethods.del_selected_user_data()   
            self.__driver.get('https://www.instagram.com/' + username + '/?__a=1')
            if not('"logging_page_id":"profilePage_' in self.__driver.page_source):
                print(Msgs.USER_NOT_FOUND)
                return
            response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
            SelectedUserData.id = str(response['graphql']['user']['id'])
            SelectedUserData.full_name = str(response['graphql']['user']['full_name'])
            SelectedUserData.username = str(response['graphql']['user']['username'])
            SelectedUserData.followed_by_viewer = str(response['graphql']['user']['followed_by_viewer'])
            SelectedUserData.is_private = str(response['graphql']['user']['is_private'])
        except Exception as e:
            Msgs.print_error(e)
    
    def deselect_user(self):
        SelectedUserMethods.del_selected_user_data()

    def get_selected_user_basic_data(self):
        if (SelectedUserData.id == ''):
            print(Msgs.SELECTED_USER_REQUIRED)
            return
        try:       
            self.__driver.get('https://www.instagram.com/' + SelectedUserData.username + '/?__a=1')
            SelectedUserMethods.set_selected_user_basic_data(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
        except Exception as e:
            Msgs.print_error(e)

    def get_selected_user_followers(self, limit = '0'):
        if (SelectedUserData.id == ''):
            print(Msgs.SELECTED_USER_REQUIRED)
            return
        if (LoggedUserData.id == ''):
            print(Msgs.LOGIN_REQUIRED)
            return
        self.__driver.get('https://www.instagram.com/' + SelectedUserData.username + '/?__a=1')
        response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
        SelectedUserData.followed_by_viewer = str(response['graphql']['user']['followed_by_viewer'])
        SelectedUserData.is_private = str(response['graphql']['user']['is_private'])
        if (SelectedUserData.followed_by_viewer == 'False') and (SelectedUserData.is_private == 'True'):
            print(Msgs.PRIVATE_ACCOUNT)
            return
        if not(limit.isnumeric()):
            print(Msgs.INVALID_ARGS)
            return
        end_cursor = ''
        next_page = True
        limit_reached = False
        limit = int(limit)
        SelectedUserData.followers_search = True
        SelectedUserData.followers_list.clear()
        count = 0
        try:
            while next_page and not(limit_reached):
                self.__driver.get('https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"' + SelectedUserData.id + '","first":50,"after":"' + end_cursor + '"}')
                response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
                for i in range(len(response['data']['user']['edge_followed_by']['edges'])):
                    follower = (response['data']['user']['edge_followed_by']['edges'][i]['node']['full_name'],response['data']['user']['edge_followed_by']['edges'][i]['node']['username'],response['data']['user']['edge_followed_by']['edges'][i]['node']['id'])
                    SelectedUserData.followers_list.append(follower)
                    count += 1
                    if (limit != '0'):
                        if (count == limit):
                            limit_reached = True
                            break            
                next_page = response['data']['user']['edge_followed_by']['page_info']['has_next_page']
                end_cursor = str(response['data']['user']['edge_followed_by']['page_info']['end_cursor'])
        except Exception as e:
            Msgs.print_error(e)

    def get_selected_user_following(self, limit = '0'):
        if (SelectedUserData.id == ''):
            print(Msgs.SELECTED_USER_REQUIRED)
            return
        if (LoggedUserData.id == ''):
            print(Msgs.LOGIN_REQUIRED)
            return
        self.__driver.get('https://www.instagram.com/' + SelectedUserData.username + '/?__a=1')
        response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
        SelectedUserData.followed_by_viewer = str(response['graphql']['user']['followed_by_viewer'])
        SelectedUserData.is_private = str(response['graphql']['user']['is_private'])
        if (SelectedUserData.followed_by_viewer == 'False') and (SelectedUserData.is_private == 'True'):
            print(Msgs.PRIVATE_ACCOUNT)
            return
        if not(limit.isnumeric()):
            print(Msgs.INVALID_ARGS)
            return
        end_cursor = ''
        next_page = True
        limit_reached = False
        limit = int(limit)
        SelectedUserData.following_search = True
        SelectedUserData.following_list.clear()
        count = 0
        try:
            while next_page and not(limit_reached):
                self.__driver.get('https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={"id":"' + SelectedUserData.id + '","first":50,"after":"' + end_cursor + '"}')
                response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
                for i in range(len(response['data']['user']['edge_follow']['edges'])):
                    followee = (response['data']['user']['edge_follow']['edges'][i]['node']['full_name'],response['data']['user']['edge_follow']['edges'][i]['node']['username'],response['data']['user']['edge_follow']['edges'][i]['node']['id'])
                    SelectedUserData.following_list.append(followee)
                    count += 1
                    if (limit != '0'):
                        if (count == limit):
                            limit_reached = True
                            break            
                next_page = response['data']['user']['edge_follow']['page_info']['has_next_page']
                end_cursor = str(response['data']['user']['edge_follow']['page_info']['end_cursor'])
        except Exception as e:
            Msgs.print_error(e)

    def get_selected_user_posts(self, limit = '0'):
        if (SelectedUserData.id == ''):
            print(Msgs.SELECTED_USER_REQUIRED)
            return
        self.__driver.get('https://www.instagram.com/' + SelectedUserData.username + '/?__a=1')
        response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
        SelectedUserData.followed_by_viewer = str(response['graphql']['user']['followed_by_viewer'])
        SelectedUserData.is_private = str(response['graphql']['user']['is_private'])
        if (SelectedUserData.followed_by_viewer == 'False') and (SelectedUserData.is_private == 'True'):
            print(Msgs.PRIVATE_ACCOUNT)
            return
        if not(limit.isnumeric()):
            print(Msgs.INVALID_ARGS)
            return
        end_cursor = ''
        next_page = True
        limit_reached = False
        limit = int(limit)
        SelectedUserData.posts_search = True
        SelectedUserData.posts_list.clear()
        count = 0
        try:
            while next_page and not(limit_reached):
                self.__driver.get('https://www.instagram.com/graphql/query/?query_hash=bfa387b2992c3a52dcbe447467b4b771&variables={"id":"' + SelectedUserData.id + '","first":50,"after":"' + end_cursor + '"}')
                response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
                for i in range(len(response['data']['user']['edge_owner_to_timeline_media']['edges'])):
                    post = (response['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['__typename'],response['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['id'],response['data']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['shortcode'])
                    SelectedUserData.posts_list.append(post)
                    count += 1
                    if (limit != '0'):
                        if (count == limit):
                            limit_reached = True
                            break            
                next_page = response['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
                end_cursor = str(response['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor'])
        except Exception as e:
            Msgs.print_error(e)

#endregion

#region "SELECTED POST"

    def select_post(self, shortcode):
        try:
            SelectedPostMethods.del_selected_post_data() 
            self.__driver.get('https://www.instagram.com/p/' + shortcode + '/?__a=1')
            if not('__typename":"' in self.__driver.page_source):
                print(Msgs.POST_NOT_FOUND)
                return
            response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
            SelectedPostData.typename = str(response['graphql']['shortcode_media']['__typename'])
            SelectedPostData.post_id = str(response['graphql']['shortcode_media']['id'])
            SelectedPostData.shortcode = str(response['graphql']['shortcode_media']['shortcode'])
            SelectedPostData.owner_full_name = str(response['graphql']['shortcode_media']['owner']['full_name'])
            SelectedPostData.owner_username = str(response['graphql']['shortcode_media']['owner']['username'])
            SelectedPostData.owner_account_id = str(response['graphql']['shortcode_media']['owner']['id'])
        except Exception as e:
            Msgs.print_error(e)

    def deselect_post(self):
        SelectedPostMethods.del_selected_post_data()

    def get_selected_post_basic_data(self):
        if (SelectedPostData.post_id == ''):
            print(Msgs.SELECTED_POST_REQUIRED)
            return
        try:       
            self.__driver.get('https://www.instagram.com/p/' + SelectedPostData.shortcode + '/?__a=1')
            SelectedPostMethods.set_selected_post_basic_data(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
        except Exception as e:
            Msgs.print_error(e)

    def get_selected_post_likes(self, limit = '0'):
        if (LoggedUserData.id == ''):
            print(Msgs.LOGIN_REQUIRED)
            return
        if (SelectedPostData.post_id == ''):
            print(Msgs.SELECTED_POST_REQUIRED)
            return
        if not(limit.isnumeric()):
            print(Msgs.INVALID_ARGS)
            return
        end_cursor = ''
        next_page = True
        limit_reached = False
        limit = int(limit)
        SelectedPostData.likers_search = True
        SelectedPostData.likers_list.clear()
        count = 0
        try:
            while next_page and not(limit_reached):
                self.__driver.get('https://www.instagram.com/graphql/query/?query_hash=d5d763b1e2acf209d62d22d184488e57&variables={"shortcode":"' + SelectedPostData.shortcode + '","first":50,"after":"' + end_cursor + '"}')
                response = json.loads(WebDriverWait(self.__driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, 'pre'))).text)
                for i in range(len(response['data']['shortcode_media']['edge_liked_by']['edges'])):
                    liker = (response['data']['shortcode_media']['edge_liked_by']['edges'][i]['node']['full_name'],response['data']['shortcode_media']['edge_liked_by']['edges'][i]['node']['username'],response['data']['shortcode_media']['edge_liked_by']['edges'][i]['node']['id'])
                    SelectedPostData.likers_list.append(liker)
                    count += 1
                    if (limit != '0'):
                        if (count == limit):
                            limit_reached = True
                            break            
                next_page = response['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
                end_cursor = str(response['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor'])
        except Exception as e:
            Msgs.print_error(e)

#endregion