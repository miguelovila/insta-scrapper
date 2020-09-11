import os

#Styles & Colours
REGULAR = '\033[2m'
BOLD = '\033[1m'
RED = '\033[91m' + '[ERROR] '
YELLOW = '\033[93m' + '[INFO] '
BLUE = '\033[36m'
DEFAULT = '\033[0m'

#Messages
INPUT_MSG = BOLD + BLUE + 'InstaScrapper > ' + DEFAULT
UNKNOWN_CMD = RED + 'Unknown command. Type ' + BOLD + 'help' + REGULAR + '.' + DEFAULT

#Methods
def print_banner():
    os.system('cls||clear')
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