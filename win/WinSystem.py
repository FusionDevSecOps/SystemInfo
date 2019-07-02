class windowsSys:

    import time
    timeStr = time.strftime("%Y%m%d-%H%M%S")
    # import subprocess
    # subprocess.Popen('ls -la', shell=True)

    # command = 'ls -la'
    def command(self, command):
        w = windowsSys()

        import subprocess
        subprocess.Popen(command + '>> sys_info.txt' + w.timeStr, shell=True)


    def command1(self, command):
        w = windowsSys()

        try:
            import subprocess
            with open('winSys_info_' + w.timeStr + '.txt', "a") as myFile:
                myFile.write("\n\nThe command that was run was\n" + command + " with output" + "\n\n")

            output = subprocess.Popen(command + '>> winSys_info_' + w.timeStr + '.txt',  stdout=subprocess.PIPE, shell=True)
            o  = output.communicate()
            # p1.stdout.close()
            print(command)
            # print(o)
            # return out
        except Exception as e:
            print(e)

    #To run to commands concurrently
    def command2(self, command1):
        import subprocess
        p1 = subprocess.Popen('powershell', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        p2 = subprocess.Popen(command1, shell=True, stdin=p1.stdout)

        p1.stdout.close()
        out, err = p2.communicate()
        print(out)
        return out, err

def main():
    win = windowsSys()


#A - Hardware inventory items like CPU size, buffer size, Memory, HDD details, Audio/sound card details, network details etc.

    #System
    win.command1('systeminfo')# >> sys_info.txt')
    win.command1('wmic cpu get caption')# >> sys_info.txt')   #processor
    #memory
    win.command1('wmic MEMORYCHIP get BankLabel, DeviceLocator, MemoryType, TypeDetail, Capacity, Speed')# >> sys_info.txt ')   # memory


    # win.command1('systeminfo | findstr /C:”Total Physical Memory"')# >> network_info.txt')    # memory       #not working
    # win.command1('systeminfo | find “Available Physical Memory”')# >> network_info.txt')    # memory         #not working


#B Software inventory items like: list of softwares installed in a machine, OS version & patch details

    win.command1( 'systeminfo | findstr /B /C:"OS Name" /C:"OS Version"')  # >> sys_info.txt ')   # memory
    win.command1( 'ver')  # >> sys_info.txt ')   # memory
    win.command1( 'wmic os get Caption,CSDVersion /value')  # >> sys_info.txt ')   # memory

    # os patches
    win.command1('powershell Get-Hotfix')  # >> sys_info.txt ')   # memory
    # win.command1('wmic qfe')  # >> sys_info.txt ')   # memory
    # win.command1('wmic qfe get Hotfixid')  # >> sys_info.txt ')   # memory

# C Driver/Firmware details like Drivers/firmware installed like Soundcard, motherboard, network
    # list drivers

    win.command1( 'driverquery')  # >> sys_info.txt ')   # memory
    win.command1( 'driverquery /FO list /v')  # Very long

# D Running servicesm
    # net start - shows window services

    win.command1( 'net start')  # Very long

# E Hostname, List of startup programs
    # hostname -- is well, the hostname
    # ipconfig /all -- all ip settings
    win.command1('hostname')  # Very long
    win.command1('ipconfig /all')  # Very long

    # wmic	- 	Windows management instrumentation command/ extremely powerfull			/? for help
    # wmic startup - start up programs
    win.command1('wmic startup')  # Very long

    # wmic product get name,version --  installed programs
    # wmic /output ............

    win.command1('wmic product get name,version ')  # Very long

# F List of mounted drives/mapped network locations
    # wmic logicaldisk get deviceid, volumename, description -- Lists mounted drives
    # wmic logicaldisk get name -
    win.command1('wmic logicaldisk get deviceid, volumename, description')  # Very long
    win.command1('wmic logicaldisk get name')  # Very long


    # net use -- mapped network drives
    # net use > mapped_drives.txt
    win.command1('net use')  # Very long

# G List of environment settings/variables
    # wmic Environment -
    # env - environmental varibales
    # SET | more - list environmental variables
    # SET > output.txt
    win.command1('wmic Environment')  # Very long
    win.command1('env')  # Very long
    win.command1('SET | more')  # Very long





    import subprocess
    # win.command2('systeminfo','findstr /C:”Total Physical Memory"' )
    # out = subprocess.Popen('systeminfo findstr /C:”Total Physical Memory"',
    #                           stdout=subprocess.PIPE,
    #                           shell=True)
    # j = out.communicate()
    # print(j)

    # output = subprocess.Popen('netstat -ano | find ":80"',
    #                           stdout=subprocess.PIPE,
    #                           shell=True)
    # o = output.communicate()
    # # print(o)




# Runs script in shell
if __name__ == '__main__':
    main()


#universal_newline