import unittest

from generate_page import extract_title


class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        result = extract_title("# Header")
        self.assertEqual(result, "Header")
        
    def test_extract_title_wrong(self):
        self.assertRaises(Exception, extract_title, "## Header")
        
    def test_extract_title_wrongi(self):
        self.assertRaises(Exception, extract_title, "#Header")
