#!/usr/bin python3

import subprocess
import pprint
import time
import json
import re
import ast
from oSCommands import oS
from JsonEdit import JsonEditer

class linux:
    timeStr = time.strftime("%Y%m%d-%H%M%S")






##A
##Hardware inventory items Cpu size, buffer size, memory, HDD details, network details

#'identifies the type of processor used by your system')  # identifies the type of processor used by your system
def Hardware():
    myDict = {}
    command = 'cat /proc/cpuinfo'
    help = 'CPU info'
    oS.command2(command)
    myDict.update(JsonEditer.twoColumns(oS.command2(command), help))

    # part of the proc virtual file system')  # part of the proc virtual file system
    command = 'cat /proc/mounts'
    help = 'Virtual File System'
    # print(oS.command2(command))
    myDict.update(JsonEditer.whiteSpaceAndBackslash(oS.command2(command), help))


    # # memory free
    command ='free'
    help = 'Memory'
    # print(oS.command2(command))
    myDict.update(JsonEditer.beforeforwardslashAndaftercolon(oS.command2(command), help))
    # print(myDict)
    return myDict


def Software():
    # # B Software inventory items like: list of softwares installed in a machine, OS version & patch details
    myDict = {}
    command = 'apt list'
    help = 'Lists all apps'
    # print(oS.command2(command))
    myDict.update(JsonEditer.beforeForwardSlashAndafterBackSlash(oS.command2(command), help))
    return myDict

def Driver_Firmware():
    # C Driver/Firmware details like Drivers/firmware installed like Soundcard, motherboard, network
    myDict = {}
    return myDict


def Services():
    # # D Running services
    myDict = {}
    command = 'systemctl list-unit-files --no-page'
    # command = 'service --status-all'
    help = ' ?'
    # print(oS.command2(command))
    myDict.update(JsonEditer.dictMethod(oS.command2(command), help))

    command = 'systemctl list-unit-files --no-page'
    # command = 'service --status-all'
    help = ' ?'
    # print(oS.command2(command))
    myDict.update(JsonEditer.beforeWhitespacesAndAfterWhitespace(oS.command2(command), help))
    return myDict


def Hostname_Startup():
    # # E Hostname, List of startup programs
    myDict = {}
    command = 'cat /proc/sys/kernel/hostname'
    help = 'Lists the host name'
    # print(oS.command2(command))
    cleanOutout = ''.join(re.sub('\n', '', oS.command2(command)))
    myDict.update({help: cleanOutout})
    return myDict



def MountedDrivers_MappedNetworks():
    # # F List of mounted drives/mapped network locations
    myDict = {}
    command = 'lsblk -o NAME,FSTYPE,SIZE,MOUNTPOINT,LABEL --json'
    help = 'Mounted drives'
    # using json loads here to pass a json formated string to a dictionary
    j_a = oS.command2(command).replace("'", "\"")
    myDict.update({help: json.loads(j_a)})
    return myDict

def Env():
    # # G List of environment settings/variables
    myDict = {}
    command = 'env'
    help = 'Lists environmental variables'
    # print(oS.command2(command))
    myDict.update(JsonEditer.beforeEqualsAndAfterEquals(oS.command2(command), help))
    return myDict




finalDict ={}

# Hardware()
finalDict.update({'Hardware' : Hardware()})
# Software()
# finalDict.update({'Software' : Software()})
# # Driver_Firmware()
# finalDict.update({'Driver_Firmware' : Driver_Firmware()})
# # Services()
# finalDict.update({'Services' : Services()})
# # Hostname_Startup()
finalDict.update({'Hostname_Startup' : Hostname_Startup()})
# MountedDrivers_MappedNetworks()
# finalDict.update({'MountedDrivers_MappedNetworks' : MountedDrivers_MappedNetworks()})
# # Env()
finalDict.update({'Env()' : Env()})

print(finalDict)

# Pretty print
# pp = pprint.PrettyPrinter(indent=4)
# s = pprint.pformat(myDict)
# j = pp.pprint(myDict)

# JsonEditer.jsonCreater(myDict)
# JsonEditer.appendAsJson(s, "json3.json")


JsonEditer.jsonCreater(finalDict, 'linux')



# def main():
#     l = linux()
#
#     l.run()
#     # if

#
# if __name__ == '__main__':
#     main()
