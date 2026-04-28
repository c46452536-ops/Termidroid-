from rich.console import Console
from rich.prompt import Prompt
from engine import highlight

console = Console()

def repl():
    while True:
        code = Prompt.ask(">")

        if code == "exit":
            break

        console.print(highlight(code))

        try:
            print(eval(code, {}))
        except:
            try:
                exec(code, {})
            except Exception as e:
                print(e)
