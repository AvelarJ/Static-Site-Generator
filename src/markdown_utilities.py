import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        elif node.text.count(delimiter) % 2 > 0:
            raise ValueError("Unmatched delimiter in text node")
        elif delimiter in node.text:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if part == "": #If first part is a match
                    continue
                if i % 2 > 0:
                    new_nodes.append(TextNode(part, text_type))                    
                else:
                    new_nodes.append(TextNode(part, TextType.TEXT))
        else:
            new_nodes.append(node)
            continue
        
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
            
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
            
    return new_nodes

    
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
                
            new_nodes.append(
                TextNode(
                    link[0],
                    TextType.LINK,
                    link[1],
                )
            )
            original_text = sections[1]
            
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
            
    return new_nodes


#First index for alt text in ![] and second for url inbetween ()
def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

#First index for link text in [] and second for url inbetween () 
def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches


#Culminating function which goes through all inline delimiters then images and links
def text_to_textnodes(text):
    if type(text) is str:
        #print("str input converted to a TextNode")
        text = TextNode(text, TextType.TEXT)
        
    delimiters = [['**', '_', '`'],[TextType.BOLD, TextType.ITALIC, TextType.CODE]]
    
    for i in range(len(delimiters[0])):
        if i == 0 and type(text) != list: #First time need to give function a list
            text = split_nodes_delimiter([text], delimiters[0][i], delimiters[1][i])
        else: #Then text will stay a list
            text = split_nodes_delimiter(text, delimiters[0][i], delimiters[1][i])
        #print(f'text now = {text}')
    
    image_check = split_nodes_image(text)
    link_check = split_nodes_link(image_check)
    return link_check


#Now converting markdown string to blocks
def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    stripped_blocks = [s.strip() for s in blocks]
    clean_blocks = [item for item in stripped_blocks if item]
    return clean_blocks
