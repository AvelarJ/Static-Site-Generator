from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from markdown_utilities import markdown_to_blocks, text_to_textnodes
from block_utilities import BlockType, block_to_block_type

def markdown_to_html_node(markdown):
    child_nodes = []
    blocks = markdown_to_blocks(markdown)
    
    for block in blocks:
        b_type = block_to_block_type(block)
        
        if b_type == BlockType.PARAGRAPH:
            children = text_to_children(block)
            para_html = ParentNode(tag = 'p', children = children)
            #print(f'Para html = {para_html}')
            child_nodes.append(para_html)
            
        elif b_type == BlockType.HEADING:
            h_count = len(block) - len(block.lstrip('#'))
            text = block.lstrip('# ')
            
            heading_html = ParentNode(tag = f'h{h_count}', children = text_to_children(text))
            child_nodes.append(heading_html)
            
        #Code is a special case: no inline should be changed/tagged
        elif b_type == BlockType.CODE:
            text = block.strip("```")
            removed_newlines = text.lstrip()
            code_text = TextNode(removed_newlines, TextType.CODE)
            code_html = ParentNode(tag = 'pre', children = [text_node_to_html_node(code_text)])
            child_nodes.append(code_html)
            
        elif b_type == BlockType.QUOTE:
            removed_newlines = block.replace("\n", " ")
            text = removed_newlines.replace('> ', '')
            
            quote_html = ParentNode(tag = 'blockquote', children=text_to_children(text))
            child_nodes.append(quote_html)
            
        elif b_type == BlockType.UNOLIST:
            uno_list = []
            
            list_items = block.split('- ')[1:]
            for li in list_items:
                removed_newlines = li.replace("\n", "")
                children = text_to_children(li)
                
                uno_list.append(ParentNode('li', children))
                
            uno_html = ParentNode(tag = 'ul', children=uno_list)
            child_nodes.append(uno_html)
            
        elif b_type == BlockType.OLIST:
            o_list = []
            #Since we know its a valid OL we can split on the . after each number
            list_items = [line.split(". ", 1)[1] for line in block.splitlines()]
            for li in list_items:
                removed_newlines = li.replace("\n", "")
                children = text_to_children(li)
                
                o_list.append(ParentNode('li', children))
                
            o_html = ParentNode(tag = 'ol', children=o_list)
            child_nodes.append(o_html)
            
        else:
            raise ValueError(f'Current block: {block}\ncannot be identified')
            
            
    return ParentNode('div', child_nodes)
            
            
            
def text_to_children(text):
    final_list = []
    removed_newlines = text.replace("\n", "")
    text_nodes = text_to_textnodes(removed_newlines)
    
    for n in text_nodes:
        final_list.append(text_node_to_html_node(n))
            
    return final_list