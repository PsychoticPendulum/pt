#! /usr/bin/env python3

import os
import sys
import json
import readline

from time import sleep

from unilog import *

# ---------------------------------------------------------------------------------------------------------------------

class cCommand:
    def __init__(self, title, function, tldr=None, example=None):
        self.title      = title
        self.function   = function
        self.tldr       = tldr
        self.example    = example

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

class cPT:

    def __init__(self):
        self.RegisterCommand(cCommand("exit",self.Exit,"Exit the program"))
        self.RegisterCommand(cCommand("clear",self.Clear,"Clear the screen"))
        self.RegisterCommand(cCommand("help",self.Help,"Display this menu"))
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
        Log(LVL.INFO, f"Registering Command: {command.title}")
        self.COMMANDS.append(command)

# ---------------------------------------------------------------------------------------------------------------------

    def SearchCommand(self, cmd):
        for command in self.COMMANDS:
            if command.title == cmd:
                return command.function
        return None

# ---------------------------------------------------------------------------------------------------------------------

    def ParseCommand(self, command):
        print(f"{UTIL.UP}{UTIL.BOLD} >> {UTIL.RESET}{FG.GREEN}{command}{UTIL.RESET}")
        cmd, arg = command, None
        if " " in command:
            cmd, arg = command.split(" ")

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
        print(f"{FG.CYAN} ╭──────────────────────────────────{UTIL.RESET}")
        for command in self.COMMANDS:
            buffer = (16 - len(command.title)) * " "
            print(f"{FG.CYAN} │ {command.title}{buffer}{command.tldr}{UTIL.RESET}")
        print(f"{FG.CYAN} ╰──────────────────────────────────{UTIL.RESET}")

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

def SayHello(args):
    print("Hello")
    
if __name__ == "__main__":
    Log(LVL.INFO, "Running pt in demo mode")

    pt = cPT()
    
    while True:
        pt.Prompt()
