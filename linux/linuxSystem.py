import subprocess
import time

class linux:


    timeStr = time.strftime("%Y%m%d-%H%M%S")

    def command(self, command):
        import subprocess
        subprocess.Popen(command, shell=True)


    def command1(self, command):
        l = linux()

        try:

            with open('LinuxSys_info_' + l.timeStr + '.txt', "a") as myFile:
                myFile.write("\n\nThe command that was run was\n" + command + "with output" + "\n\n")

            output = subprocess.Popen(command + '>> LinuxSys_info_' + l.timeStr + '.txt', stdout=subprocess.PIPE,shell=True)
            o = output.communicate()
            # p1.stdout.close()
            print(command)
            # return out
        except Exception as e:
            print(e)

        # To run to commands concurrently

    def command2(self, command2):
        import subprocess
        p1 = subprocess.Popen('sudo' , shell=True, stdin=None, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        p2 = subprocess.Popen(command2, shell=True, stdin=p1.stdout)

        p1.stdout.close()
        out, err = p2.communicate()
        print(out)
        return out, err


    def run(self):
        l = linux()

        #List the hardware and add to a text file
        l.command2('apt-get update')
        l.command2('apt-get install lshw')
        # l.command1('sudo lshw -short')
        # l.command1('lshw > linux/linuxSysInfo.txt')

        l.command2('lshw ')


        l.command1('apt-get update')
        l.command1('apt-get install hwinfo')
        l.command1('hwinfo --short')      #

        #memory free
        l.command1('free')



# B Software inventory items like: list of softwares installed in a machine, OS version & patch details
#         l.command1('apt list')
        l.command1('lsb_release -a ')

# C Driver/Firmware details like Drivers/firmware installed like Soundcard, motherboard, network
        l.command1('service --status-all')

#D Running services
        l.command1('service --status-all')

        # l.command1('ls -1 /lib/systemd/system/*.service /etc/systemd/system/*.service ')


#E Hostname, List of startup programs
        l.command1('cat /proc/sys/kernel/hostname')

        # l.command1('find / -name "*autostart*" ')
        # l.command1('ls -1 "/etc/xdg/autostart" "/home/$USER/.config/autostart" "/usr/share/gdm/autostart"  "/usr/share/gnome/autostart" ')


#F List of mounted drives/mapped network locations
        # l.command1('lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL ')   #failure to access sysfs /sys/dev/block


#G List of environment settings/variables
        l.command1('printenv')
        l.command1('env ')




def main():
    l = linux()

    l.run()
    # if



if __name__ == '__main__':
    main()