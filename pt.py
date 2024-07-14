#! /usr/bin/env python3

import os
import sys
import json
import readline

from time import sleep

from unilog import *

# ---------------------------------------------------------------------------------------------------------------------

class cCommand:
    def __init__(self, title, function, category="default", tldr=None, example=None):
        self.title      = title
        self.function   = function
        self.category   = category
        self.tldr       = tldr
        self.example    = example

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

class cPT:

    def __init__(self):
        self.RegisterCommand(cCommand("exit",self.Exit,"System","Exit the program"))
        self.RegisterCommand(cCommand("clear",self.Clear,"System","Clear the screen"))
        self.RegisterCommand(cCommand("help",self.Help,"System","Display this menu"))
        print(f"{UTIL.CLEAR}")

# ---------------------------------------------------------------------------------------------------------------------

    COMMANDS = []
    LOGO = [
        f"       _    ",
        f" _ __ | |_  ",
        f"| '_ \\| __|",
        f"| |_) | |_  ",
        f"| .__/ \\__|",
        f"|_|         "
    ]

# ---------------------------------------------------------------------------------------------------------------------

    def SetLogo(self, logo):
        if type(logo) == list:
            self.LOGO = logo
        else:
            Log(LVL.WARN, "SetLogo(): Invalid Datatype!")

# ---------------------------------------------------------------------------------------------------------------------

    def RegisterCommand(self, command):
        self.COMMANDS.append(command)
        self.COMMANDS = sorted(self.COMMANDS, key=lambda COMMAND: (COMMAND.category != 'System', COMMAND.category))

# ---------------------------------------------------------------------------------------------------------------------

    def SearchCommand(self, cmd):
        for command in self.COMMANDS:
            if command.title == cmd:
                return command.function
        return None

# ---------------------------------------------------------------------------------------------------------------------

    def ParseCommand(self, command):
        cmd, arg = command, None
        if " " in command:
            cmd, arg = command.split(" ", 1)
        print(f"{UTIL.UP}{UTIL.BOLD} >> {UTIL.RESET}{FG.GREEN}{cmd}{UTIL.RESET} {arg}")

        function = self.SearchCommand(cmd)

        if function != None:    function(arg)
        elif cmd == "":         print(f"{UTIL.UP}{UTIL.CLEARLINE}")
        else:                   print(f"{UTIL.UP}{UTIL.BOLD} >> {UTIL.RESET}{FG.RED}{command}{UTIL.RESET}")
    
# ---------------------------------------------------------------------------------------------------------------------

    def Prompt(self):
        print(f"{UTIL.TOP}",end="")
        for line in self.LOGO:
            print(f"{UTIL.CLEARLINE}{UTIL.BOLD}{FG.BLUE} {line}{UTIL.RESET}")

        for i in range(os.get_terminal_size().lines - len(self.LOGO)):
            print(f"{UTIL.DOWN}",end="")

        command = input(f"{UTIL.BOLD} >> {UTIL.RESET}") 
        self.ParseCommand(command)

# ---------------------------------------------------------------------------------------------------------------------

    def Exit(self, exit_code):
        print(f"{UTIL.CLEAR}{UTIL.TOP}",end="")
        sys.exit(exit_code)

# ---------------------------------------------------------------------------------------------------------------------

    def Clear(self, args):
        print(f"{UTIL.CLEAR}{UTIL.TOP}",end="")

# ---------------------------------------------------------------------------------------------------------------------

    def Help(self, args):
        sym     = "─"
        first   = True
        last    = ""
        for command in self.COMMANDS:
            buffer = (32 - len(command.category)) * sym
            if first:
                print(f"{FG.CYAN} ╭──── {UTIL.RESET}{UTIL.BOLD}{command.category}{UTIL.RESET}{FG.CYAN} {buffer}{UTIL.RESET}")
                first   = False
                last    = command.category
            elif last != command.category:
                print(f"{FG.CYAN} ├──── {UTIL.RESET}{UTIL.BOLD}{command.category}{UTIL.RESET}{FG.CYAN} {buffer}{UTIL.RESET}")
                last    = command.category
            buffer = (16 - len(command.title)) * " "
            print(f"{FG.CYAN} │ {UTIL.RESET}{UTIL.BOLD}{command.title}{UTIL.RESET}{buffer}{command.tldr}{UTIL.RESET}")
        print(f"{FG.CYAN} ╰──────────────────────────────────────{UTIL.RESET}")

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    Log(LVL.INFO, "Running pt in demo mode")

    pt = cPT()

    while True:
        pt.Prompt()
