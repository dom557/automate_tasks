import unittest
import os
import shutil
from automate_tasks.file_management import create_directory, delete_directory, copy_file, move_file

class TestFileManagement(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_dir'
        self.test_file = 'test_file.txt'
        self.copied_file = 'copied_file.txt'
        create_directory(self.test_dir)
        with open(os.path.join(self.test_dir, self.test_file), 'w') as f:
            f.write('test')

    def tearDown(self):
        delete_directory(self.test_dir)
        if os.path.exists(self.copied_file):
            os.remove(self.copied_file)

    def test_create_and_delete_directory(self):
        create_directory('another_test_dir')
        self.assertTrue(os.path.exists('another_test_dir'))
        delete_directory('another_test_dir')
        self.assertFalse(os.path.exists('another_test_dir'))

    def test_copy_file(self):
        copy_file(os.path.join(self.test_dir, self.test_file), self.copied_file)
        self.assertTrue(os.path.exists(self.copied_file))

    def test_move_file(self):
        move_file(os.path.join(self.test_dir, self.test_file), self.copied_file)
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, self.test_file)))
        self.assertTrue(os.path.exists(self.copied_file))

if __name__ == '__main__':
    unittest.main()
