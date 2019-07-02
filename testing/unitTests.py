import unittest

from Exercise2 import OsCheck


class TestOsCheck(unittest.TestCase):

    def test_os(self):
        os = OsCheck.systemCheck()


        self.assertEqual(os.platfrom(), "Windows", "Should be Windows")





class TestKey_Nouns(unittest.TestCase):

    def test_sum_tuple(self):
        self.assertEqual(sum((2, 2, 2)), 6, "Should be 6")

class TestKey_Retrieve_sort_compare(unittest.TestCase):


    def test_sum_tuple(self):
        self.assertEqual(sum((2, 2, 2)), 6, "Should be 6")






if __name__ == '__main__':
    unittest.main()