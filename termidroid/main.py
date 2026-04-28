import os
from python.repl import repl
from nano.nano import nano
from micro.micro import micro
from git.git import init, commit, log

cwd = "/home"

def shell():
    global cwd
    print("MiniOS Terminal (Termux-like core)")

    while True:
        cmd = input(f"{cwd}$ ").strip()

        # ---------------- HELP ----------------
        if cmd == "help":
            print("""
Core commands:
 ls
 cd <folder>
 pwd
 cat <file>
 echo <text>
 clear
 python
 nano
 micro
 git init <name>
 git commit <name> <msg>
 git log <name>
 exit
""")

        # ---------------- EXIT ----------------
        elif cmd == "exit":
            break

        # ---------------- CLEAR ----------------
        elif cmd == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        # ---------------- PWD ----------------
        elif cmd == "pwd":
            print(cwd)

        # ---------------- ECHO ----------------
        elif cmd.startswith("echo"):
            print(cmd[5:])

        # ---------------- LS ----------------
        elif cmd == "ls":
            print("bin  home  pkg  plugins")

        # ---------------- CD ----------------
        elif cmd.startswith("cd"):
            folder = cmd.split(" ")[1] if len(cmd.split()) > 1 else "/home"
            cwd = folder

        # ---------------- CAT ----------------
        elif cmd.startswith("cat"):
            print("[simulated file output]")

        # ---------------- PYTHON ----------------
        elif cmd == "python":
            repl()

        # ---------------- NANO ----------------
        elif cmd == "nano":
            nano()

        # ---------------- MICRO ----------------
        elif cmd == "micro":
            micro()

        # ---------------- GIT ----------------
        elif cmd.startswith("git init"):
            init(cmd.split()[2])

        elif cmd.startswith("git commit"):
            parts = cmd.split()
            commit(parts[2], " ".join(parts[3:]))

        elif cmd.startswith("git log"):
            log(cmd.split()[2])

        # ---------------- UNKNOWN ----------------
        else:
            print("command not found")

shell()
