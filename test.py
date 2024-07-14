#! /usr/bin/env python3

from math import *
from pt import *

def SysCall(args):
    os.system(args)

def Test(args):
    print("Test")

if __name__ == "__main__":
    pt = cPT()
    pt.RegisterCommand(cCommand("test",Test,"Test","Test0"))
    pt.RegisterCommand(cCommand("syscall",SysCall,"Local","Run a command on the system","syscall <command>","syscall echo Hello World"))

    logo = [
        " _____ _____ ____ _____ ____  _   _ ___ _____ _____ ",
        "|_   _| ____/ ___|_   _/ ___|| | | |_ _|_   _| ____|",
        "  | | |  _| \___ \ | | \___ \| | | || |  | | |  _|  ",
        "  | | | |___ ___) || |  ___) | |_| || |  | | | |___ ",
        "  |_| |_____|____/ |_| |____/ \___/|___| |_| |_____|"

    ]

    pt.SetLogo(logo)
    while True:
        pt.Prompt()
