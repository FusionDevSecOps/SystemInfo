#!/usr/bin python3

from sys import platform


# import WinSystem


class systemCheck:

    def run(self, command):
        import subprocess
        subprocess.Popen(command, shell=True)

    def command2(self, command1, command2):
        import subprocess
        p1 = subprocess.Popen(command1, shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # input("Press Enter to continue...")
        p2 = subprocess.Popen(command2, shell=True, stdin=p1.stdout)

        p1.stdout.close()
        out, err = p2.communicate()
        print(out)
        return out, err

    # s = systemCheck()
    def platfrom(self):
        s = systemCheck()

        if platform == "linux" or platform == "linux2":
            print("linux\n")

            command = 'chmod +x linux/linuxSystem.py'
            s.run(command)
            command = 'sudo python3 linux/linuxSystem.py'
            s.run(command)

        # s.command("sudo python linux/linuxSystem.py")
        # import subprocess
        # subprocess.Popen(command, shell=True)
        # # l.main()

        elif platform == "win32":
            print("Windows\n")

    # from Exercise2.win import WinSystem

            command = 'python win\WinSystem.py'
            s.run(command)


def main():
    s = systemCheck()
    s.platfrom()


if __name__ == '__main__':
    main()
