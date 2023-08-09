# Copy Right 2023 Ali Crafty
# START
import os, sys
try:
    def cd(path):
        try:
            os.system(f"cd {path}")
        except:
            pass
    def dir():
        try:
            os.system("ls")
        except:
            pass
    def cls():
        try:
            os.system("clear")
        except:
            pass
    run = True
    path = os.getcwd()
    while run:
        cmd = str(input(f"{path}>"))
        if("cd" in cmd):
            cmd = cmd.split(" ")
            if(cmd[0]=="cd"):
                cd(cmd[1])
        elif("dir" in cmd):
            cmd = cmd.split(" ")
            if(cmd[0]=="dir"):
                dir()
        elif("cls" in cmd):
            cmd = cmd.split(" ")
            if(cmd[0]=="cls"):
                cls()
        elif("^E" in cmd):
            cmd = cmd.split(" ")
            if(cmd[0]=="^E"):
                sys.exit()
except:
    pass
# END