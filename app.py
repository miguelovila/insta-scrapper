import common.terminal_messages as Msgs
from bot import Driver as Driver
import readline

Msgs.print_banner()
driver = Driver(False)
while True:
    try:
        cmd, *arg = str.split(input(Msgs.INPUT_MSG).lower())
    except:
        print(Msgs.UNKNOWN_CMD)
        continue

    if cmd == '':
        pass
    elif cmd == 'clear' or cmd == 'cls':
        Msgs.print_banner()
    elif cmd == 'quit' or cmd == 'exit' or cmd == 'close':
        break
    else:
        print(Msgs.UNKNOWN_CMD)

del driver