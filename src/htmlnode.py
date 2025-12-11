'''
An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes
'''


class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
        
    def to_html(self):
        raise NotImplementedError("to_html is not impletmented yet")
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str
    
"""
It should not allow for any children (The whole point of a leaf)
Both the value and tag data members should be required 
(even though the tag's value may be None), while props can remain optional like the HTMLNode constructor."""

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
"""
The tag and children arguments are not optional
It doesn't take a value argument
props is optional
(It's the exact opposite of the LeafNode class)"""

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        elif not self.children:
            raise ValueError("Parent nodes must have children")
        else:
            opening_tag = f"<{self.tag}{self.props_to_html()}>"
            closing_tag = f"</{self.tag}>"
            children_html = "".join([child.to_html() for child in self.children])
            return f"{opening_tag}{children_html}{closing_tag}"