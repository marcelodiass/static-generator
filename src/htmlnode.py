class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        html_props = ""
        
        for prop in self.props:
            html_props += f' {prop}="{self.props[prop]}"'
        
        return html_props
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("You must provide the argument tag.")
        if self.children is None:
            raise ValueError("You must provide the argument children.")
        
        node_children = ""
        for child in self.children:
            node_children += child.to_html()
        
        if self.props is None:
            return f"<{self.tag}>{node_children}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{node_children}</{self.tag}>"
