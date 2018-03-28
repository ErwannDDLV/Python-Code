import unittest
import ls_2
import os

# run test file with :
# python3 -m unittest test_ls_2.py


class TestLs2(unittest.TestCase):

    def test_file_list(self):
        result = ls_2.file_list('/Users/erwann/code/ErwannDDLV/Python-code/testing-folder/')
        self.assertEqual([
                'aa-test.doc',
                'aa-two-test.txt',
                'bb-test.txt',
                'new-test-file.xls',
                'test-two.doc',
                'test.doc',
                'test.txt',
                'test.xls'
        ], result)

if __name__ == '__main__':
    unittest.main()