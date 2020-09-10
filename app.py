import common.messages as Messages
import readline

Messages.print_banner()
while True:
    cmd, *arg = str.split(input(Messages.__INPUT_MSG).lower())
    if cmd == 'sel':
        pass
    elif cmd == 'clear' or cmd == 'cls':
        Messages.print_banner()
    elif cmd == 'quit' or cmd == 'exit' or cmd == 'close':
        break
    else:
        print(Messages.__UNKNOWN_CMD)