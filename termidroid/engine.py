from rich.syntax import Syntax

def detect_lang(code):
    if "<html" in code:
        return "html"
    elif "function" in code or "console.log" in code:
        return "javascript"
    elif "import" in code or "def " in code:
        return "python"
    return "python"

def highlight(code):
    return Syntax(code, detect_lang(code), theme="monokai", line_numbers=True)
