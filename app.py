import readline
import common.terminal_messages as Msgs
import loggedin_user.methods as LoggedUserMethods
import selected_user.methods as SelectedUserMethods
import selected_post.methods as SelectedPostMethods
from bot import Driver
import os

Msgs.print_banner()
driver = Driver(False)

while True:
    try:
        cmd, *args = str.split(input(Msgs.INPUT_MSG))
        cmd = cmd.lower()
    except:
        print(Msgs.UNKNOWN_CMD)
        continue

    if (cmd == 'get'):
        args = [x.lower() for x in args]

        if (len(args) < 1) or (len(args)>3):
            print(Msgs.INVALID_ARGS)
            continue
        
        if (args[0] == 'logged-user'):
            if (len(args) == 2):
                if (args[1] == 'basic-data'):
                    driver.get_logged_user_basic_data()
                    LoggedUserMethods.show_logged_user_basic_data()
                    continue
                if (args[1] == 'following-list'):
                    driver.get_logged_user_following()
                    LoggedUserMethods.show_logged_user_following_list()
                    continue
                if (args[1] == 'followers-list'):
                    driver.get_logged_user_followers()
                    LoggedUserMethods.show_logged_user_followers_list()
                    continue
                if (args[1] == 'posts-list'):
                    driver.get_logged_user_posts()
                    LoggedUserMethods.show_logged_user_posts_list
                    continue
                print(Msgs.INVALID_ARGS)
                continue
            if (len(args) == 3):
                if (args[1] == 'following-list'):
                    driver.get_logged_user_following(args[2])
                    LoggedUserMethods.show_logged_user_following_list()
                    continue
                if (args[1] == 'followers-list'):
                    driver.get_logged_user_followers(args[2])
                    LoggedUserMethods.show_logged_user_followers_list()
                    continue
                if (args[1] == 'posts-list'):
                    driver.get_logged_user_posts(args[2])
                    LoggedUserMethods.show_logged_user_posts_list()
                    continue
                print(Msgs.INVALID_ARGS)
                continue

        if (args[0] == 'selected-user'):
            if (len(args) == 2):
                if (args[1] == 'basic-data'):
                    driver.get_selected_user_basic_data()
                    SelectedUserMethods.show_selected_user_basic_data()
                    continue
                if (args[1] == 'following-list'):
                    driver.get_selected_user_following()
                    SelectedUserMethods.show_selected_user_following_list
                    continue
                if (args[1] == 'followers-list'):
                    driver.get_selected_user_followers()
                    SelectedUserMethods.show_selected_user_followers_list
                    continue
                if (args[1] == 'posts-list'):
                    driver.get_selected_user_posts()
                    SelectedUserMethods.show_selected_user_posts_list()
                    continue
                print(Msgs.INVALID_ARGS)
                continue
            if (len(args) == 3):
                if (args[1] == 'following-list'):
                    driver.get_selected_user_following(args[2])
                    SelectedUserMethods.show_selected_user_following_list()
                    continue
                if (args[1] == 'followers-list'):
                    driver.get_selected_user_followers(args[2])
                    SelectedUserMethods.show_selected_user_followers_list
                    continue
                if (args[1] == 'posts-list'):
                    driver.get_selected_user_posts(args[2])
                    SelectedUserMethods.show_selected_user_posts_list()
                    continue
                print(Msgs.INVALID_ARGS)
                continue

        if (args[0] == 'selected-post'):
            if (len(args) == 2):
                if (args[1] == 'basic-data'):
                    driver.get_selected_post_basic_data()
                    SelectedPostMethods.show_selected_post_basic_data()
                    continue
                if (args[1] == 'likers-list'):
                    driver.get_selected_post_likes()
                    SelectedPostMethods.show_selected_post_likers_list
                    continue
                print(Msgs.INVALID_ARGS)
                continue
            if (len(args) == 3):
                if (args[1] == 'likers-list'):
                    driver.get_selected_post_likes(args[2])
                    SelectedPostMethods.show_selected_post_likers_list()
                    continue
                print(Msgs.INVALID_ARGS)
                continue

        print(Msgs.INVALID_ARGS)
        continue

    if (cmd == 'show'):
        args = [x.lower() for x in args]

        if (len(args) < 1) or (len(args)>2):
            print(Msgs.INVALID_ARGS)
            continue
        
        if (args[0] == 'logged-user'):
            if (len(args) == 1):
                LoggedUserMethods.show_logged_user()
                continue
            if (len(args) == 2):
                if (args[1] == 'basic-data'):
                    LoggedUserMethods.show_logged_user_basic_data()
                    continue
                if (args[1] == 'following-list'):
                    LoggedUserMethods.show_logged_user_following_list()
                    continue
                if (args[1] == 'followers-list'):
                    LoggedUserMethods.show_logged_user_followers_list()
                    continue
                if (args[1] == 'posts-list'):
                    LoggedUserMethods.show_logged_user_posts_list()
                    continue
                print(Msgs.INVALID_ARGS)
                continue

        if (args[0] == 'selected-user'):
            if (len(args) == 1):
                SelectedUserMethods.show_selected_user()
                continue
            if (len(args) == 2):
                if (args[1] == 'basic-data'):
                    SelectedUserMethods.show_selected_user_basic_data()
                    continue
                if (args[1] == 'following-list'):
                    SelectedUserMethods.show_selected_user_following_list()
                    continue
                if (args[1] == 'followers-list'):
                    SelectedUserMethods.show_selected_user_followers_list()
                    continue
                if (args[1] == 'posts-list'):
                    SelectedUserMethods.show_selected_user_posts_list()
                    continue
                print(Msgs.INVALID_ARGS)
                continue

        if (args[0] == 'selected-post'):
            if (len(args) == 1):
                SelectedPostMethods.show_selected_post()
                continue
            if (len(args) == 2):
                if (args[1] == 'basic-data'):
                    SelectedPostMethods.show_selected_post_basic_data()
                    continue
                if (args[1] == 'likers-list'):
                    SelectedPostMethods.show_selected_post_likers_list()
                    continue
                print(Msgs.INVALID_ARGS)
                continue

        print(Msgs.INVALID_ARGS)
        continue

    if (cmd == 'auth') or (cmd=='login'):
        if len(args) != 2:
            print(Msgs.INVALID_ARGS)
            continue 
        driver.auth(args)
        continue

    if (cmd == 'deauth') or (cmd=='logout'):
        if len(args) != 0:
            print(Msgs.INVALID_ARGS)
            continue 
        driver.deauth()
        continue

    if (cmd == 'select') or (cmd=='sel'):

        if len(args) != 2:
            print(Msgs.INVALID_ARGS)
            continue

        if (args[0].lower() == 'user'):
            driver.select_user(args[1])
            continue

        if (args[0].lower() == 'post'):
            driver.select_post(args[1])
            continue

        print(Msgs.INVALID_ARGS)
        continue

    if (cmd == 'deselect') or (cmd=='desel'):
        args = [x.lower() for x in args]

        if len(args) != 1:
            print(Msgs.INVALID_ARGS)
            continue

        if (args[0] == 'user'):
            driver.deselect_user()
            continue

        if (args[0] == 'post'):
            driver.deselect_post()
            continue

        print(Msgs.INVALID_ARGS)
        continue

    if (cmd == 'cls') or (cmd == 'clear'):
        if len(args) != 0:
            print(Msgs.INVALID_ARGS)
            continue 
        os.system('cls||clear')
        Msgs.print_banner()
        continue

    if (cmd == 'quit') or (cmd=='exit') or (cmd == 'close'):
        if len(args) != 0:
            print(Msgs.INVALID_ARGS)
            continue 
        break

    print(Msgs.UNKNOWN_CMD)

del driver