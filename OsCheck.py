from sys import platform
from oSCommands import oS
# import WinSystem


class systemCheck:

    def platfrom(self):

        s = systemCheck()

        if platform == "linux" or platform == "linux2":
            print("linux\n")

            command = 'python3 jsonFormattedLinuxCommands.py'

            oS.commandLinux(command)


        elif platform == "win32":
            print("Windows\n")

            command = 'python jsonFormattedWindowsCommands.py'

            oS.command2(command)



def main():
    s = systemCheck()
    s.platfrom()


if __name__ == '__main__':
    main()