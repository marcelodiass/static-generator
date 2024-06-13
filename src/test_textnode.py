import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
        
    def test_text_to_html(self):
        node = TextNode("Normal text", "text")
        self.assertEqual(node.to_html(), "Normal text")
        
    def test_bold_to_html(self):
        node = TextNode("Bold text", "bold")
        self.assertEqual(node.to_html(), "<b>Bold text</b>")
    
    def test_link_to_html(self):
        node = TextNode("Link text", "link", "google.com")
        self.assertEqual(node.to_html(), '<a href="google.com">Link text</a>')
        
    def test_image_to_html(self):
        node = TextNode("Image Alt Text", "image", "google.com")
        self.assertEqual(node.to_html(), '<img src="google.com" alt="Image Alt Text"></img>')
        
    
    
if __name__ == "__main__":
    unittest.main()