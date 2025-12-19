from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNOLIST = 'unordered_list'
    OLIST = 'ordered_list'
    
    
def block_to_block_type(markdown):
    if re.findall(r'^#{1,6} .+', markdown):
        return BlockType.HEADING
    elif re.findall(r'^(```|~~~)', markdown):
        return BlockType.CODE
    elif re.findall(r'^>+ .+', markdown):
        return BlockType.QUOTE
    elif re.findall(r'^- .+', markdown):
        return BlockType.UNOLIST
    
    #For ordered list need numbers to start at 1. and increment by 1 each time
    #Also need to be careful to have no newline char or anything after EOL
    elif re.findall(r'^\d+\. .+', markdown):
        split_olist = markdown.split('\n')
        #print(f'Split Ordered List = {split_olist}')
        if is_valid_ordered_list(split_olist):
            return BlockType.OLIST
        else:
            print("ORDERED LIST NOT IN ORDER")
            return BlockType.PARAGRAPH

    else:
        return BlockType.PARAGRAPH
    
#Used to make sure ordered list starts at 1. and increments
def is_valid_ordered_list(lines):
    pattern = r'^(\d+)\. .+'
    expected = 1
    for line in lines:
        match = re.match(pattern, line)
        if not match:
            return False
        number = int(match.group(1))
        if number != expected:
            return False
        expected += 1
    return True