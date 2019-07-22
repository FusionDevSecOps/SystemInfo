import unittest
from sys import platform
import OsCheck
import oSCommands
from oSCommands import oS
from jsonFormattedWindowsCommands import winSys
from JsonEdit import JsonEditer
from jsonFormattedLinuxCommands import linux

class TestOsCheck(unittest.TestCase):

    def test_os(self):
        os = OsCheck.systemCheck()
        a = platform
        self.assertEqual(os.platfrom(), platform)


class TestOsCommands(unittest.TestCase):
    from oSCommands import oS


    def test_command2(self):

        self.assertIsInstance(oS.command2("system"), str)
        # self.assertEqual(oS.command2(), )

    def test_commandWin(self):

        self.assertIsInstance(oS.command2("system"), str)
        # self.assertEqual(oS.command2(), )

    def test_commandLinux(self):

        self.assertIsInstance(oS.command2("system"), str)
        # self.assertEqual(oS.command2(), )



class TestFormattedWindowsCommands(unittest.TestCase):
    from jsonFormattedWindowsCommands import winSys

    if platform == platform == "win32":

        def test_Hardware(self):
            self.assertIsInstance(winSys.Hardware(self), dict)

        def test_Software(self):
            self.assertIsInstance(winSys.Software(self), dict)

        def test_Firmware(self):
            self.assertIsInstance(winSys.Driver_Firmware(self), dict)

        def test_Services(self):
            self.assertIsInstance(winSys.Services(self), dict)

        def test_Hostname_Startup(self):
            self.assertIsInstance(winSys.Hostname_Startup(self), dict)

        def test_MountedDrivers_MappedNetworks(self):
            self.assertIsInstance(winSys.MountedDrivers_MappedNetworks(self), dict)

        def test_Env(self):
            self.assertIsInstance(winSys.Env(self), dict)

    else:
        print(platform + "platform not compatable with current tests " )





class TestJsonEdit(unittest.TestCase):
    from jsonFormattedWindowsCommands import winSys


    def test_JsonEdit(self):
        self.assertIsInstance(JsonEditer.dictMethod(self, "hello"), dict)

    def test_twoColumns(self):
        self.assertIsInstance(JsonEditer.twoColumns( "hello", "hello"), dict)

    def test_beforeEqualsAndAfterEquals(self):
        self.assertIsInstance(JsonEditer.beforeEqualsAndAfterEquals("hello", "hello"), dict)

    def test_beforeForwardSlashAndafterBackSlash(self):
        self.assertIsInstance(JsonEditer.beforeForwardSlashAndafterBackSlash("hello", "hello"), dict)

    def test_beforeForwardSlashAndafterBackSlash(self):
        self.assertIsInstance(JsonEditer.beforeforwardslashAndaftercolon("hello", "hello"), dict)

    def beforeWhitespacesAndAfterWhitespace(self):
        self.assertIsInstance(JsonEditer.beforeWhitespacesAndAfterWhitespace("hello", "hello"), dict)


class TestJsonFormattedLinuxCommands(unittest.TestCase):

    if platform == "linux" or platform == "linux2":

        def test_Hardware(self):
            self.assertIsInstance(linux.Hardware(self), dict)

        def test_Software(self):
            self.assertIsInstance(linux.Software(self), dict)

        def test_Firmware(self):
            self.assertIsInstance(linux.Driver_Firmware(self), dict)

        def test_Services(self):
            self.assertIsInstance(linux.Services(self), dict)

        def test_Hostname_Startup(self):
            self.assertIsInstance(linux.Hostname_Startup(self), dict)

        def test_MountedDrivers_MappedNetworks(self):
            self.assertIsInstance(linux.MountedDrivers_MappedNetworks(self), dict)

        def test_Env(self):
            self.assertIsInstance(linux.Env(self), dict)


    else:
        print(platform + "platform not compatable with current tests " )







if __name__ == '__main__':
    unittest.main()