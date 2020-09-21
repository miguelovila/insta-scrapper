import urllib.request

#Styles & Colours
REGULAR = '\033[2m'
BOLD = '\033[1m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[36m'
DEFAULT = '\033[0m'

#Messages
INPUT_MSG = BOLD + BLUE + 'InstaScrapper > ' + DEFAULT
UNKNOWN_CMD = RED + '[ERROR] Unknown command. Type ' + BOLD + 'help' + REGULAR + '.' + DEFAULT
UNKNOWN_ERROR = RED + '[ERROR] Unknown error. Type ' + BOLD + 'help' + REGULAR + '.' + DEFAULT
INVALID_ARGS = RED + '[ERROR] Invalid arguments for given command. Type ' + BOLD + 'help' + REGULAR + '.' + DEFAULT
INVALID_CARDENTIALS = RED + '[ERROR] Invalid cardentials. Type ' + BOLD + 'help' + REGULAR + '.' + DEFAULT 
NO_DATA_TO_SHOW = RED + '[ERROR] All data is empty. First run "get" command or type ' + BOLD + 'help' + REGULAR + '.' + DEFAULT 
SELECTED_USER_REQUIRED = RED + '[ERROR] The user must be selected. Type ' + BOLD + 'help' + REGULAR + '.' + DEFAULT
SELECTED_POST_REQUIRED = RED + '[ERROR] The post must be selected. Type ' + BOLD + 'help' + REGULAR + '.' + DEFAULT
USER_NOT_FOUND = RED + '[ERROR] The user does not exist.' + DEFAULT
POST_NOT_FOUND = RED + '[ERROR] The post does not exist or is private.' + DEFAULT
PRIVATE_ACCOUNT = RED + '[ERROR] The user has a private account and isn\'t followed by you.' + DEFAULT
LOGIN_REQUIRED = RED + '[ERROR] The user must be authenticated. Type ' + BOLD + 'help' + REGULAR + '.' + DEFAULT

#Methods
def shrink_url(url):
    try:
        apiurl = "http://tinyurl.com/api-create.php?url="
        tinyurl = urllib.request.urlopen(apiurl + url).read()
        return tinyurl.decode("utf-8")
    except:
        return 'None'

def remove_last_line_from_string(s):
    return s[:s.rfind('\n')]

def print_info(content):
    print(YELLOW + '[INFO] ' + str(content) + DEFAULT)

def print_error(content):
    print(RED + '[ERROR] ' + str(content) + DEFAULT)

def print_banner():
    print(DEFAULT)
    print(r'      ____           __            _____                                        ')    
    print(r'     /  _/___  _____/ /_____ _    / ___/______________ _____  ____  ___  _____  ')
    print(r'     / // __ \/ ___/ __/ __ `/    \__ \/ ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/  ')
    print(r'   _/ // / / (__  ) /_/ /_/ /    ___/ / /__/ /  / /_/ / /_/ / /_/ /  __/ /      ')
    print(r'  /___/_/ /_/____/\__/\__,_/    /____/\___/_/   \__,_/ .___/ .___/\___/_/       ')
    print(r'                                                    /_/   /_/              1.0  ')
    print(r'                                                                                ')
    print(r'           Author: Miguel Vila       E-Mail: miguel.vila.dev@gmail.com          ')
    print(r'                                                                                ')
    print(r'================================================================================')
    print(r'                                                                                ')