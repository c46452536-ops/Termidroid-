import sys
import termios
import tty
from engine import highlight
from rich.console import Console

console = Console()

def get_key():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)

    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

    return ch


def nano():
    console.print("[green]Nano Editor[/green]")
    console.print("[yellow]Ctrl+S = Save | Ctrl+X = Exit[/yellow]\n")

    lines = []
    buffer = ""

    while True:
        ch = get_key()

        # ENTER
        if ch in ["\n", "\r"]:
            lines.append(buffer)
            buffer = ""
            console.print(highlight("\n".join(lines)))

        # BACKSPACE
        elif ord(ch) == 127:
            buffer = buffer[:-1]
            print("\r" + buffer + " ", end="", flush=True)

        # CTRL + S (SAVE)
        elif ch == "\x13":
            console.print("\n[green]Saved![/green]")
            return "\n".join(lines)

        # CTRL + X (EXIT)
        elif ch == "\x18":
            console.print("\n[red]Exited without saving[/red]")
            return None

        else:
            buffer += ch
            print(ch, end="", flush=True)
