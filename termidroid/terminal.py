import sys, termios, tty

class TerminalInput:
    def input(self, prompt="$ "):
        print(prompt, end="", flush=True)
        buf = ""

        while True:
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)

            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)

            if ch in ["\n", "\r"]:
                print()
                return buf

            elif ord(ch) == 127:
                buf = buf[:-1]
                print("\r$ " + buf + " ", end="", flush=True)

            elif ch == "\x03":
                print("\n^C")
                return ""

            else:
                buf += ch
                print(ch, end="", flush=True)
