import common.terminal_messages as Msgs
import selected_user.data as SelectedUserData
import json

#Writting Data
def set_selected_user_basic_data(response):
    response = json.loads(response)
    SelectedUserData.biography = str(response['graphql']['user']['biography'])
    SelectedUserData.external_url = str(response['graphql']['user']['external_url'])
    SelectedUserData.followers = str(response['graphql']['user']['edge_followed_by']['count'])
    SelectedUserData.following = str(response['graphql']['user']['edge_follow']['count'])
    SelectedUserData.full_name = str(response['graphql']['user']['full_name'])
    SelectedUserData.id = str(response['graphql']['user']['id'])
    SelectedUserData.is_business_account = str(response['graphql']['user']['is_business_account'])
    SelectedUserData.business_category = str(response['graphql']['user']['business_category_name'])
    SelectedUserData.is_private = str(response['graphql']['user']['is_private'])
    SelectedUserData.is_verified = str(response['graphql']['user']['is_verified'])
    SelectedUserData.profile_pic_url = str(Msgs.shrink_url(response['graphql']['user']['profile_pic_url_hd']))
    SelectedUserData.username = str(response['graphql']['user']['username'])
    SelectedUserData.uploads = str(response['graphql']['user']['edge_owner_to_timeline_media']['count'])

def del_selected_user_data():
    SelectedUserData.biography = ''
    SelectedUserData.external_url = ''
    SelectedUserData.followers = ''
    SelectedUserData.following = ''
    SelectedUserData.full_name = ''
    SelectedUserData.id = ''
    SelectedUserData.is_business_account = ''
    SelectedUserData.business_category = ''
    SelectedUserData.is_private = ''
    SelectedUserData.is_verified = ''
    SelectedUserData.profile_pic_url = ''
    SelectedUserData.username = ''
    SelectedUserData.uploads = ''
    SelectedUserData.followers_search = False
    SelectedUserData.followers_list.clear()
    SelectedUserData.following_search = False
    SelectedUserData.following_list.clear()
    SelectedUserData.posts_search = False
    SelectedUserData.posts_list.clear()
    SelectedUserData.followed_by_viewer = ''

#Showing Data
def show_selected_user():
    if SelectedUserData.id == '':
        print(Msgs.SELECTED_USER_REQUIRED)
        return
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Full Name: ',SelectedUserData.full_name) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Username: ',SelectedUserData.username) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Account ID: ',SelectedUserData.id) + Msgs.DEFAULT)

def show_selected_user_basic_data():
    if SelectedUserData.id == '':
        print(Msgs.SELECTED_USER_REQUIRED)
        return
    if SelectedUserData.is_verified == '':
        print(Msgs.NO_DATA_TO_SHOW)
        return
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Biography: ',SelectedUserData.biography.replace('\n',f'\n{"[INFO]":<26}')) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Website: ',SelectedUserData.external_url) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Followers: ',SelectedUserData.followers) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Following: ',SelectedUserData.following) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Full Name: ',SelectedUserData.full_name) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Account ID: ',SelectedUserData.id) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Is Business: ',SelectedUserData.is_business_account) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Category: ',SelectedUserData.business_category) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Is Private: ',SelectedUserData.is_private) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Is Verified: ',SelectedUserData.is_verified) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Profile Picture: ',SelectedUserData.profile_pic_url) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Username: ',SelectedUserData.username) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Posts: ',SelectedUserData.uploads) + Msgs.DEFAULT)

def show_selected_user_following_list():
    if SelectedUserData.id == '':
        print(Msgs.SELECTED_USER_REQUIRED)
        return
    if SelectedUserData.following_search == False:
        print(Msgs.NO_DATA_TO_SHOW)
        return
    first = True
    for followee in SelectedUserData.following_list:
        if not(first):
            print (Msgs.YELLOW + "[INFO]" + Msgs.DEFAULT)
        else:
            first = False
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Full Name: ',followee[0]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Username: ',followee[1]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Account ID: ',followee[2]) + Msgs.DEFAULT)

def show_selected_user_followers_list():
    if SelectedUserData.id == '':
        print(Msgs.SELECTED_USER_REQUIRED)
        return
    if SelectedUserData.followers_search == False:
        print(Msgs.NO_DATA_TO_SHOW)
        return
    first = True
    for follower in SelectedUserData.followers_list:
        if not(first):
            print (Msgs.YELLOW + "[INFO]" + Msgs.DEFAULT)
        else:
            first = False
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Full Name: ',follower[0]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Username: ',follower[1]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Account ID: ',follower[2]) + Msgs.DEFAULT)

def show_selected_user_posts_list():
    if SelectedUserData.id == '':
        print(Msgs.SELECTED_USER_REQUIRED)
        return
    if SelectedUserData.posts_search == False:
        print(Msgs.NO_DATA_TO_SHOW)
        return
    first = True
    for post in SelectedUserData.posts_list:
        if not(first):
            print (Msgs.YELLOW + "[INFO]" + Msgs.DEFAULT)
        else:
            first = False
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Type Name: ',post[0]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Post ID: ',post[1]) + Msgs.DEFAULT)
        print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Short Code: ',post[2]) + Msgs.DEFAULT)