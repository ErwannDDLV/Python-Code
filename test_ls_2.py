import unittest
import ls_2
import os
import stat
import time

from datetime import datetime 

# run test file with :
# python3 test_ls_2.py

class TestFileList(unittest.TestCase):

    def test_file_list(self):
        path = "/Users/erwann/code/ErwannDDLV/Python-Code/testing-folder/"
        files_list = []

        if os.path.isdir(path):
            for file in os.listdir(path):
                if os.path.isfile(os.path.join(path, file)) and not file.startswith('.'):
                    files_list.append(file)
            self.assertEqual(files_list, [
                'aa-test.doc',
                'aa-two-test.txt',
                'bb-test.txt',
                'new-test-file.xls',
                'test-two.doc',
                'test.doc',
                'test.txt',
                'test.xls'
            ])
            self.assertNotEqual(files_list, [
                'aa-test.doc',
                'test-two.doc',
                'test.doc',
                'test.txt',
                'test.xls'
            ])       

        else:
            for file in glob.glob(path + 't*.*', recursive=True):
                    files_list.append(file)
            self.assertEqual(files_list, [
                'test-two.doc',
                'test.doc',
                'test.txt',
                'test.xls'
            ])
            self.assertNotEqual(files_list, [
                'aa-test.doc',
                'aa-two-test.txt',
                'bb-test.txt',
                'new-test-file.xls',
            ])       

    def test_file_list_mode(self):
        path = "/Users/erwann/code/ErwannDDLV/Python-Code/testing-folder/"
        files_list = []

        for file in os.listdir(path):
            pathname = os.path.join(path, file)
            permissions = stat.filemode(os.stat(pathname).st_mode)
            created_date = datetime.fromtimestamp(os.stat(pathname).st_ctime).date()
            if os.path.isfile(pathname) and not file.startswith('.'):
                files_list.append(file)
        self.assertEqual(files_list, [
            'aa-test.doc',
            'aa-two-test.txt',
            'bb-test.txt',
            'new-test-file.xls',
            'test-two.doc',
            'test.doc',
            'test.txt',
            'test.xls'
        ])

if __name__ == '__main__':
    unittest.main()

