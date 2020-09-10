import common.terminal_messages as Msgs
import readline

Msgs.print_banner()
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