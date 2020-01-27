from sys import platform
from src.main.python.oSCommands import oS
# import WinSystem


class systemCheck:

    def platfrom(self):

        s = systemCheck()

        if platform == "linux" or platform == "linux2":
            print("Linux\n")

            command = 'python3 LinuxCommands.py'

            oS.commandLinux(command)


        elif platform == "win32":
            print("Windows\n")

            command = 'python WindowsCommands.py'

            oS.command2(command)

        return platform



def main():
    s = systemCheck()
    s.platfrom()


if __name__ == '__main__':
    main()