from JsonEdit import JsonEditer
from oSCommands import oS
import json
import re


class winSys:
    # timeStr = time.strftime("%Y%m%d-%H%M%S")
    myDict = {}
    # jsonEdit = JsonEditer()

    # jsonEdit.dictMethod()


    # def powerShellConvertToJson(input):
    #     # input = 'wmic cpu get caption | ConvertTo-Json'
    #     command = 'powershell ' + '" '+  input +  '| ConvertTo-Json"'
    #     # command ='powershell.exe Get - WmiObject - class ' + '" '+  input +  '| ConvertTo-Json"'
    #     oS.command2(command)
    #     # oS.command2(command)
    #     a = oS.command2(command)
    #     # print(a)
    #     return a
    #

    def powerShellConvertToJson(input):
        command = 'powershell.exe ' +  input + '| ConvertTo-Json'
        return oS.commandWin(command)

    # A Hardware inventory items like CPU size, buffer size, Memory, HDD details, Audio/sound card details, network details etc.
    def Hardware(self):
        myDict = {}
        command = 'systeminfo'
        help = 'System Info'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        # command = 'wmic cpu get caption'
        # help = 'Cpu'
        # myDict.update({help: json.loads(powerShellConvertToJson(command))})

        command = 'Get-WmiObject -class Win32_processor | select-object Name, DeviceID, NumberOfCores, NumberOfEnabledCore, NumberOfLogicalProcessors, L2CacheSize,L3CacheSize,MaxClockSpeed,CurrentClockSpeed,Addresswidth'
        help = 'CPU'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        # command = 'wmic PATH Win32_videocontroller GET description'
        # help = 'VideoCard'
        # myDict.update({help: json.loads(powerShellConvertToJson(command))})


        # command = 'wmic MEMORYCHIP get BankLabel, DeviceLocator, MemoryType, TypeDetail, Capacity, Speed'
        # help = 'Memory'
        # myDict.update({help: json.loads(powerShellConvertToJson(command))})

        # command = 'Win32_PhysicalMemory | ''  select-object ' 'Name, ' 'ConfiguredClockSpeed,' ' Capacity, ''TotalWidth, ''SerialNumber '
        # help = 'Memory'
        # myDict.update({help: json.loads(powerShellConvertToJson(command))})

        # command = 'systeminfo | findstr /B /C:"OS Name" /C:"OS Version"'
        # help = 'VideoCard'
        # myDict.update({help: json.loads(powerShellConvertToJson(command))})

        return myDict

    # B Software inventory items like: list of softwares installed in a machine, OS version & patch details
    # winver
#     command = 'ver'
#     help = 'Windows version'
#     myDict.update({help: json.loads(powerShellConvertToJson(command))})
    def Software(self):
        myDict = {}
        command = 'Get-WmiObject -class win32_operatingsystem | Select-Object '
        'Name, '
        'OSArchitecture, '
        'BuildNumber,'
        'Version, '
        'ServicePackMajorVersion, '
        'ServicePackMinorVersion'
        help = 'operatingsystem'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        # os patches
        command = 'Get-Hotfix'  # >> sys_info.txt ')   # memory
        help = 'os patches'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        #need powershell for this
        command = 'wmic qfe'
        help = 'Windows hotfixes'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        command = 'wmic qfe get Hotfixid'
        help = 'Windows hotfixes'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        return myDict

    # C Driver/Firmware details like Drivers/firmware installed like Soundcard, motherboard, network
    # list drivers
    def Driver_Firmware(self):
        myDict = {}
        command = 'driverquery'
        help = 'Driver list'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        command = 'driverquery /FO list /v'
        help = 'Driver list'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        command ='Get-WmiObject -class Win32_PnPSignedDriver | select-object '
        'devicename, '
        'driverversion'
        help = 'Driver list'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})
        return myDict

    # D Running servicesm
    # net start - shows window services
    def Services(self):
        myDict = {}
        command = 'net start'
        help = 'Window services'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        command ='Get-WmiObject -class win32_process | select-object'
        'ProcessName, '
        'ProcessId, '
        'PageFaults '
        help = 'Running Process'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        return myDict

    # E Hostname, List of startup programs
    # hostname -- is well, the hostname
    # ipconfig /all -- all ip settings
    def Hostname_Startup(self):
        myDict = {}
        command = 'hostname'
        help = 'Hostname'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        command = 'ipconfig /all'
        help = 'Ip serivces'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        # wmic	- 	Windows management instrumentation command/ extremely powerfull			/? for help
        # wmic startup - start up programs
        command = 'wmic startup'
        help = 'Startup programs'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        command = 'Get-WmiObject -class Win32_StartupCommand | '
        'select-object  '
        'Description, '
        'Location, '
        'User'
        help = 'Startup programs'
        # myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        # wmic product get name,version --  installed programs
        command = 'Get-WmiObject -class Get - WmiObject - Class Win32_Product'
        help = 'Installed programs'
        # myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        command = 'Get-WmiObject -class Win32_Product | Select-Object '
        'Name, '
        'PackageCode,'
        'IdentifyingNumber, '
        'PackageCache,  '
        'Vendor, '
        'Version, '
        'InstallSource,'
        'InstallDate,'
        'InstallDate2 '
        help = 'Installed programs'
        # myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})
        return myDict


    # F List of mounted drives/mapped network locations
    def MountedDrivers_MappedNetworks(self):
        myDict = {}
        command = 'Get-WmiObject -class Win32_LogicalDisk | select-object '
        'Name,'
        'Description, '
        'Size,'
        'FreeSpace,'
        'DriveType'
        help = 'Mounted drives'
        # myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        command = 'Get-WmiObject -class wmic logicaldisk get deviceid, volumename, description'
        help = 'mounted drives/mapped network locations'
        # myDict.update({help: json.loads(powerShellConvertToJson(command))})

        command = 'Get-WmiObject -class wmic logicaldisk get name'
        help = 'mounted drives/mapped network locations'
        # myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        # net use -- mapped network drives
        # net use > mapped_drives.txt
        command = 'net use'
        help = 'Mapped network drives'
        # myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        command = 'Get-WmiObject -class Win32_NetworkAdapter | select-object '
        'MACAddress,'
        'ProductName,'
        'ServiceName,'
        'TimeOfLastReset,  '
        'AdapterType,'
        'AdapterTypeId,'
        'AutoSense,'
        'Caption,'
        'ConfigManagerErrorCode,'
        'ConfigManagerUserConfig,'
        'CreationClassName,'
        'Description,'
        'ErrorCleared,'
        'ErrorDescription,'
        'GUID,'
        'Index,'
        'InstallDate,'
        'Installed,'
        'InterfaceIndex,'
        'LastErrorCode,'
        'Manufacturer,'
        'MaxNumberControlled,'
        'MaxSpeed,'
        'Manufacturer,'
        'MaxNumberControlled,'
        'MaxSpeed,'
        'NetConnectionID,'
        'NetConnectionStatus,'
        'NetEnabled,'
        'NetworkAddresses,'
        'PermanentAddress,'
        'PhysicalAdapter,'
        'PowerManagementCapabilities'
        help = 'NetworkAdapter'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})


        return myDict

    # G List of environment settings/variables
    def Env(self):
        myDict = {}
        command = 'Get-WmiObject -class win32_Environment'
        help = 'Environment variables'
        # myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})


        command = 'Get-WmiObject -class Win32_Environment | '
        'select-object '
        'Name, '
        'VariableValue'
        help = 'Environment variables'
        # myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        command = 'env'
        help = 'Environment variables'
        myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})
        #
        command = 'SET | more'
        help = 'Environment variables'
        # myDict.update({help: json.loads(winSys.powerShellConvertToJson(command))})

        return myDict



finalDict ={}

# winSys().Hardware()
finalDict.update({'Hardware' : winSys().Hardware()})
# winSys().Software()
# finalDict.update({'Software' : winSys().Software()})
# # Driver_Firmware()
# finalDict.update({'Driver_Firmware' : winSys().Driver_Firmware()})
# # Services()
# finalDict.update({'Services' : winSys().Services()})
# # Hostname_Startup()
# finalDict.update({'Hostname_Startup' : winSys().Hostname_Startup()})
# # # MountedDrivers_MappedNetworks()
# finalDict.update({'MountedDrivers_MappedNetworks' : winSys().MountedDrivers_MappedNetworks()})
# # # # Env()
# finalDict.update({'Env' : winSys().Env()})

print(finalDict)

JsonEditer.jsonCreater(finalDict, 'windows')

# Pretty print
import pprint
# pp = pprint.PrettyPrinter(indent=4)
# s = pprint.pformat(finalDict)
# j = pp.pprint(s)
