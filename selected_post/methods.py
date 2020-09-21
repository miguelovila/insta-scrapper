import common.terminal_messages as Msgs
import selected_post.data as SelectedPostData
import json

#Writting Data
def set_selected_post_basic_data(response):
    SelectedPostData.tagged_users = ''
    response = json.loads(response)
    del_selected_post_data()
    SelectedPostData.typename = str(response['graphql']['shortcode_media']['__typename'])
    SelectedPostData.post_id = str(response['graphql']['shortcode_media']['id'])
    SelectedPostData.shortcode = str(response['graphql']['shortcode_media']['shortcode'])
    for i in range(len(response['graphql']['shortcode_media']['edge_media_to_tagged_user']['edges'])):
        SelectedPostData.tagged_users += (response['graphql']['shortcode_media']['edge_media_to_tagged_user']['edges'][i]['node']['user']['username']) + ' \n'
    for i in range(len(response['graphql']['shortcode_media']['edge_media_to_caption']['edges'])):
        SelectedPostData.caption += (response['graphql']['shortcode_media']['edge_media_to_caption']['edges'][i]['node']['text']) + '\n'
    SelectedPostData.likes = str(response['graphql']['shortcode_media']['edge_media_preview_like']['count'])
    SelectedPostData.owner_full_name = str(response['graphql']['shortcode_media']['owner']['full_name'])
    SelectedPostData.owner_username = str(response['graphql']['shortcode_media']['owner']['username'])
    SelectedPostData.owner_account_id = str(response['graphql']['shortcode_media']['owner']['id'])

def del_selected_post_data():
    SelectedPostData.typename = ''
    SelectedPostData.post_id = ''
    SelectedPostData.shortcode = ''
    SelectedPostData.tagged_users = ''
    SelectedPostData.caption = ''
    SelectedPostData.likes = ''
    SelectedPostData.owner_full_name = ''
    SelectedPostData.owner_username = ''
    SelectedPostData.owner_account_id = ''

#Showing Data
def show_selected_post():
    if SelectedPostData.post_id == '':
        print(Msgs.SELECTED_POST_REQUIRED)
        return
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Post Type: ',SelectedPostData.typename) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Short Code: ',SelectedPostData.shortcode) + Msgs.DEFAULT)
    print (Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Owner Account: ',SelectedPostData.owner_username) + Msgs.DEFAULT)

def show_selected_post_basic_data():
    if SelectedPostData.likes == '':
        print(Msgs.NO_DATA_TO_SHOW)
        return
    print(Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Post Type: ', SelectedPostData.typename) + Msgs.DEFAULT) 
    print(Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Post ID: ',SelectedPostData.post_id) + Msgs.DEFAULT)
    print(Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Short Code: ',SelectedPostData.shortcode) + Msgs.DEFAULT)
    print(Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Tagged Users: ',Msgs.remove_last_line_from_string(SelectedPostData.tagged_users.replace(' \n',f'\n{"[INFO]":<26}'))) + Msgs.DEFAULT)
    print(Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Caption Text: ',Msgs.remove_last_line_from_string(SelectedPostData.caption)) + Msgs.DEFAULT)
    print(Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Likes: ',SelectedPostData.likes) + Msgs.DEFAULT)
    print(Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Owner Name: ', SelectedPostData.owner_full_name) + Msgs.DEFAULT)
    print(Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Owner Username: ',SelectedPostData.owner_username) + Msgs.DEFAULT)
    print(Msgs.YELLOW + "[INFO] {:>18} {:<18}".format('Owner ID: ',SelectedPostData.owner_account_id) + Msgs.DEFAULT)