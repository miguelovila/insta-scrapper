import common.terminal_messages as Msgs
from bot import Driver as Driver
import readline

Msgs.print_banner()
driver = Driver(True)
while True:
    try:
        cmd, *args = str.split(input(Msgs.INPUT_MSG))
        cmd = cmd.lower()
    except:
        print(Msgs.UNKNOWN_CMD)
        continue

    if cmd == '':
        pass
    elif cmd == 'auth' or cmd == 'login':
        driver.auth(args)
    elif cmd == 'deauth' or cmd == 'logout':
        driver.deauth(args)
    elif cmd == 'clear' or cmd == 'cls':
        Msgs.print_banner()
    elif cmd == 'quit' or cmd == 'exit' or cmd == 'close':
        break
    else:
        print(Msgs.UNKNOWN_CMD)

del driver