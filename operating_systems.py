import os

os.chdir("/home/nsk")
for dirs in os.listdir():
    if  not dirs.startswith("."):
        print(dirs)

print(os.system("cat /etc/os-release"))
print(os.getcwd())
