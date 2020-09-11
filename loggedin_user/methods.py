import common.terminal_messages as Msgs
import loggedin_user.data as LoggedUserData
import json

def store_logged_user_data(response):
    try:
        response = json.loads(response)
        LoggedUserData.full_name = response['graphql']['user']['full_name']
    except:
        print(Msgs.UNKNOWN_ERROR)

def clear_logged_user_data():
    try:
        LoggedUserData.full_name = ''
    except:
        print(Msgs.UNKNOWN_ERROR)