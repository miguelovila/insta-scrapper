import common.terminal_messages as Msgs
import loggedin_user.data as LoggedUserData
import json

def get_logged_user_basic_data():
    if LoggedUserData.username == '':
        print(Msgs.LOGIN_REQUIRED)
        return
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Biography: ',LoggedUserData.biography.replace('\n',f'\n{"[INFO]":<26}')) + Msgs.DEFAULT) 
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('E-Mail: ',LoggedUserData.business_email) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Website: ',LoggedUserData.external_url) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Followers: ',LoggedUserData.followers) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Following: ',LoggedUserData.following) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Full Name: ',LoggedUserData.full_name) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Account ID: ',LoggedUserData.id) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Is Business: ',LoggedUserData.is_business_account) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Category: ',LoggedUserData.business_category) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Is Private: ',LoggedUserData.is_private) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Is Verified: ',LoggedUserData.is_verified) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Profile Picture: ',LoggedUserData.profile_pic_url) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Username: ',LoggedUserData.username) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Posts: ',LoggedUserData.uploads) + Msgs.DEFAULT)

def get_logged_user_followers_list():
    first = True
    for follower in LoggedUserData.followers_list:
        if not(first):
            print (Msgs.YELLOW + "[INFO]" + Msgs.DEFAULT)
        else:
            first = False
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Full Name: ',follower[0]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Username: ',follower[1]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Account ID: ',follower[2]) + Msgs.DEFAULT)

def get_logged_user_following_list():
    first = True
    for followee in LoggedUserData.following_list:
        if not(first):
            print (Msgs.YELLOW + "[INFO]" + Msgs.DEFAULT)
        else:
            first = False
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Full Name: ',followee[0]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Username: ',followee[1]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Account ID: ',followee[2]) + Msgs.DEFAULT)

def get_logged_user_posts_list():
    first = True
    for post in LoggedUserData.posts_list:
        if not(first):
            print (Msgs.YELLOW + "[INFO]" + Msgs.DEFAULT)
        else:
            first = False
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Type Name: ',post[0]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Post ID: ',post[1]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Short Code: ',post[2]) + Msgs.DEFAULT)

def get_logged_user():
    if LoggedUserData.username == '':
        print(Msgs.LOGIN_REQUIRED)
        return
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Full Name: ',LoggedUserData.full_name) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Username: ',LoggedUserData.username) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Account ID: ',LoggedUserData.id) + Msgs.DEFAULT)

def set_logged_user_data(response):
    response = json.loads(response)
    LoggedUserData.biography = str(response['graphql']['user']['biography'])
    LoggedUserData.business_email = str(response['graphql']['user']['business_email'])
    LoggedUserData.external_url = str(response['graphql']['user']['external_url'])
    LoggedUserData.followers = str(response['graphql']['user']['edge_followed_by']['count'])
    LoggedUserData.following = str(response['graphql']['user']['edge_follow']['count'])
    LoggedUserData.full_name = str(response['graphql']['user']['full_name'])
    LoggedUserData.id = str(response['graphql']['user']['id'])
    LoggedUserData.is_business_account = str(response['graphql']['user']['is_business_account'])
    LoggedUserData.business_category = str(response['graphql']['user']['business_category_name'])
    LoggedUserData.is_private = str(response['graphql']['user']['is_private'])
    LoggedUserData.is_verified = str(response['graphql']['user']['is_verified'])
    LoggedUserData.profile_pic_url = str(Msgs.shrink_url(response['graphql']['user']['profile_pic_url_hd']))
    LoggedUserData.username = str(response['graphql']['user']['username'])
    LoggedUserData.uploads = str(response['graphql']['user']['edge_owner_to_timeline_media']['count'])

def del_logged_user_data():
    LoggedUserData.biography = ''
    LoggedUserData.business_email = ''
    LoggedUserData.external_url = ''
    LoggedUserData.followers = ''
    LoggedUserData.following = ''
    LoggedUserData.full_name = ''
    LoggedUserData.id = ''
    LoggedUserData.is_business_account = ''
    LoggedUserData.business_category = ''
    LoggedUserData.is_private = ''
    LoggedUserData.is_verified = ''
    LoggedUserData.profile_pic_url = ''
    LoggedUserData.username = ''
    LoggedUserData.uploads = ''
    LoggedUserData.followers_list.clear()
    LoggedUserData.following_list.clear()
    LoggedUserData.posts_list.clear()