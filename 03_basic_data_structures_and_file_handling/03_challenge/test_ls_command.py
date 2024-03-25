import io
import os
import unittest
from unittest.mock import patch


class TestOrganizeFiles(unittest.TestCase):
    test_dir = "test_directory"

    def setUp(self):
        os.makedirs(self.test_dir, exist_ok=True)
        for i in range(10):
            open(os.path.join(self.test_dir, f"{i}.py"), "a").close()
        for i in range(5):
            open(os.path.join(self.test_dir, f"{i}.cpp"), "a").close()
        open(os.path.join(self.test_dir, "1.txt"), "a").close()

    def test_organize_files(self):

        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            from ls_command import ls_command

            ls_command(self.test_dir)

            expected_output = "Summary in alphabetical order:\n.cpp:5 files\n.py:10 files\n.txt:1 file"

            actual_output = mock_stdout.getvalue().strip()

            self.assertEqual(expected_output, actual_output)

    def tearDown(self):
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)


if __name__ == "__main__":
    unittest.main()