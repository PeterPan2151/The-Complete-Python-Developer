import unittest
import main

class TextMain(unittest.TestCase):
    def test_do_stuff(self):
        test_num = 10
        result = main.do_stuff(test_num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_num = 'hahaha'
        result = main.do_stuff(test_num)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter number')

if __name__ is '__main__':
    unittest.main()

