#! /usr/bin/env python3

from pt import *

def SysCall(args):
    os.system(args)

def Test(args):
    print("Test")

if __name__ == "__main__":
    pt = cPT()
    pt.RegisterCommand(cCommand("test",Test,"Test"))
    pt.RegisterCommand(cCommand("syscall",SysCall,"Run a command on the system"))

    logo = [
        " __  __  ____ ____ ",
        "|  \/  |/ ___/ ___|",
        "| |\/| | |  | |    ",
        "| |  | | |__| |___ ",
        "|_|  |_|\____\____|"
    ]

    pt.SetLogo(logo)
    while True:
        pt.Prompt()
