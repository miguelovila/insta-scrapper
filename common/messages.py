import os

#Styles & Colours
__REGULAR = '\033[2m'
__BOLD = '\033[1m'
__RED = '\033[91m'
__YELLOW = '\033[93m'
__BLUE = '\033[36m'
__DEFAULT = '\033[0m'

#Messages
__INPUT_MSG = __BOLD + __BLUE + 'InstaScrapper > ' + __DEFAULT
__UNKNOWN_CMD = __RED + 'Unknown command. Type ' + __BOLD + 'help' + __REGULAR + '.'

#Methods
def print_banner():
    os.system('cls||clear')
    print(__DEFAULT)
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