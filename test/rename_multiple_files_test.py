import unittest
from unittest.mock import patch
import rename_multiple_files
import os


PATH = os.path.join(os.getcwd(), 'test')


class Test_rename_multiple_files(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ patch('os.listdir')
    def test_get_folder_content(self, mock_listdir):
        """
        Test that it can get contents in folder
        """
        global PATH
        rename_multiple_files.get_folder_content(PATH)
        mock_listdir.assert_called_once_with(PATH)

    @ patch('os.path.isfile')
    @ patch('os.path.join')
    def test_get_files_in_folder(self,   mock_path_isfile, mock_path_join):
        """
        Test that it can get all files in folder
        """
        global PATH
        rename_multiple_files.get_files_in_folder(PATH)
        mock_path_isfile.assert_called()
        mock_path_join.assert_called()

    @ patch('os.rename')
    def test_rename_file(self, mock_rename):
        """
        Test that it can rename a file
        """
        global PATH
        path = os.path.join(PATH, 'pattern.txt')
        callPath = os.path.join(PATH, 'new_name.txt')
        pattern = 'pattern'
        new_name = 'new_name'
        rename_multiple_files.rename_file(path, pattern, new_name)
        mock_rename.assert_called_once_with(path, callPath)


if __name__ == '__main__':
    unittest.main()
