import common.terminal_messages as Msgs
import selected_post.data as SelectedPostData
import json

#Writting Data
def set_selected_post_basic_data(response):
    pass
def del_selected_post_data():
    SelectedPostData.typename = ''
    SelectedPostData.post_id = ''
    SelectedPostData.shortcode = ''
    SelectedPostData.tagged_users = ''
    SelectedPostData.caption = ''
    SelectedPostData.comments = ''
    SelectedPostData.likes = ''
    SelectedPostData.owner_full_name = ''
    SelectedPostData.owner_username = ''
    SelectedPostData.owner_account_id = ''