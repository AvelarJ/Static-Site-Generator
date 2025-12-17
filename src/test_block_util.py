import unittest

from block_utilities import BlockType, block_to_block_type
from textnode import TextNode, TextType

class TestBlockUtil(unittest.TestCase):
    
    def test_blocktype_heading(self):
        text = """# Heading with 1 hash
## Heading with 2 hash
### Heading with 3 hash
"""
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.HEADING)
        
    def test_blocktype_code(self):
        text = """```Code block```
"""
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.CODE)
        
    def test_blocktype_quote(self):
        text = """> First quote
> Second quote
"""
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.QUOTE)
        
    def test_blocktype_unordered_list(self):
        text = """- Example list
- No order is needed
- This is a list
"""
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.UNOLIST)
        
    def test_blocktype_ordered_list(self):
        text = """1. First part of list
2. Second part
3. Last part of list"""
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.OLIST)
        
    def test_blocktype_ordered_list_wrong(self):
        text = """1. First part of list
3. Second part
5. Last part of list"""
        result = block_to_block_type(text)
        self.assertNotEqual(result, BlockType.OLIST)
        
    def test_blocktype_quote_wrong(self):
        text = """>First quote
> Second quote
"""
        result = block_to_block_type(text)
        self.assertNotEqual(result, BlockType.QUOTE)
        
    def test_blocktype_unordered_list_wrong(self):
        text = """-Example list
-No order is needed
- This is a list
"""
        result = block_to_block_type(text)
        self.assertNotEqual(result, BlockType.UNOLIST)