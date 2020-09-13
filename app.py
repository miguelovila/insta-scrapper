import readline
import common.terminal_messages as Msgs
import loggedin_user.methods as LoggedUserMethods
from bot import Driver

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
            if (len(args) == 1):
                LoggedUserMethods.get_logged_user()
                continue
            if (len(args) == 2):
                if (args[1] == 'basic-data'):
                    LoggedUserMethods.get_logged_user_basic_data()
                    continue
                if (args[1] == 'following-list'):
                    #LoggedUserMethods.get_logged_user_following()
                    continue
                if (args[1] == 'followers-list'):
                    driver.set_logged_user_followers()
                    continue
                if (args[1] == 'posts-list'):
                    #LoggedUserMethods.get_logged_user_posts()
                    continue
                print(Msgs.INVALID_ARGS)
                continue
            if (len(args) == 3):
                if (args[1] == 'following-list'):
                    #LoggedUserMethods.get_logged_user_following(args[2])
                    continue
                if (args[1] == 'followers-list'):
                    driver.set_logged_user_followers(args[2])
                    continue
                if (args[1] == 'posts-list'):
                    #LoggedUserMethods.get_logged_user_posts(args[2])
                    continue
                print(Msgs.INVALID_ARGS)
                continue

        if (args[0] == 'selected-user'):
            continue

        if (args[0] == 'selected-post'):
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

    if (cmd == 'cls') or (cmd == 'clear'):
        if len(args) != 0:
            print(Msgs.INVALID_ARGS)
            continue 
        Msgs.print_banner()
        continue

    if (cmd == 'quit') or (cmd=='exit') or (cmd == 'close'):
        if len(args) != 0:
            print(Msgs.INVALID_ARGS)
            continue 
        break

    print(Msgs.UNKNOWN_CMD)

del driver






"""
    elif cmd == 'get':
        if (len(args) > 0):
                print(Msgs.INVALID_ARGS)
                return 
"""

"""
args = [x.lower() for x in args]
        if (len(args) < 1) or (len(args) > 3):
                print(Msgs.INVALID_ARGS)
        elif args[0] == 'logged-user':
            args.pop(0)
            if (len(args) > 1):
                print(Msgs.INVALID_ARGS)
                continue
            if len(args) == 0:
                LoggedUserMethods.get_logged_user()
            elif len(args) == 1:
                if args[0] == 'basic-data':
                    LoggedUserMethods.get_logged_user_data()
                else:
                    print(Msgs.INVALID_ARGS)
            else:
                print(Msgs.INVALID_ARGS)
        elif args[0] == 'selected-user':
            pass
        else:
            print(Msgs.INVALID_ARGS)
"""