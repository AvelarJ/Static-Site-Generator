from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_utilities import split_nodes_delimiter, extract_markdown_images, split_nodes_image, split_nodes_link, text_to_textnodes

def main():
    
    text = TextNode("`First` word as a code block", TextType.TEXT)
    result = split_nodes_delimiter([text], '`', TextType.CODE)
    print(result)
    
    
    
if __name__ == "__main__":
    main()