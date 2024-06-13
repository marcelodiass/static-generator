from htmlnode import LeafNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )
        
        
    def to_html(self):
        text_type = self.text_type
        if text_type == "text":
            return LeafNode(tag=None, value=self.text).to_html()
        elif text_type == "bold":
            return LeafNode(tag="b", value=self.text).to_html()
        elif text_type == "italic":
            return LeafNode(tag="i", value=self.text).to_html()
        elif text_type == "code":
            return LeafNode(tag="code", value=self.text).to_html()
        elif text_type == "link":
            return LeafNode(tag="a", value=self.text, props={"href": self.url}).to_html()
        elif text_type == "image":
            return LeafNode(tag="img", value="", props={"src": self.url, "alt": self.text}).to_html()
              

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"