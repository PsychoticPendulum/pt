#! /usr/bin/env python3

import os
import sys
import json
import readline

from unilog import *

# ---------------------------------------------------------------------------------------------------------------------

class cCommand:
    def __init__(self, title, function, category="default", tldr=None, synopsis=None, example=None):
        self.title      = title
        self.function   = function
        self.category   = category
        self.tldr       = tldr
        self.synopsis   = synopsis
        self.example    = example

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------

class cPT:

    def __init__(self):
        self.RegisterCommand(cCommand("exit",self.Exit,"System","Exit the program","exit","exit"))
        self.RegisterCommand(cCommand("clear",self.Clear,"System","Clear the screen","clear","clear"))
        self.RegisterCommand(cCommand("help",self.Help,"System","Display this menu","help","help"))
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
                return command
        return None

# ---------------------------------------------------------------------------------------------------------------------

    def ParseCommand(self, command):
        cmd, args = command, None
        if " " in command:
            cmd, args = command.split(" ", 1)
        print(f"{UTIL.UP}{UTIL.BOLD} >> {UTIL.RESET}{FG.GREEN}{cmd}{UTIL.RESET} {args}")

        command = self.SearchCommand(cmd)

        if args != None and args == "?":
            print(f"{FG.RED} │ {UTIL.RESET}{UTIL.BOLD}Title:          {UTIL.RESET}{command.title}")
            print(f"{FG.RED} │ {UTIL.RESET}{UTIL.BOLD}TLDR:           {UTIL.RESET}{command.tldr}")
            print(f"{FG.RED} │ {UTIL.RESET}{UTIL.BOLD}Synopsis:       {UTIL.RESET}{command.synopsis}")
            print(f"{FG.RED} │ {UTIL.RESET}{UTIL.BOLD}Example:        {UTIL.RESET}{command.example}")
            return

        if command != None: command.function(args)
        elif cmd == "":     print(f"{UTIL.UP}{UTIL.CLEARLINE}")
        else:               print(f"{UTIL.UP}{UTIL.BOLD} >> {UTIL.RESET}{FG.RED}{command}{UTIL.RESET}")
    
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

    def Exit(self, args):
        print(f"{UTIL.CLEAR}{UTIL.TOP}",end="")
        sys.exit(args)

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
