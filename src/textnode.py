from enum import Enum
from htmlnode import HtmlNode

class TextType(Enum):
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'
    TEXT = 'text'

class TextNode:
    def __init__(self, text, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    def to_html_node(self):
        if self.text_type == TextType.BOLD:
            return HtmlNode(tag="bold", value=self.text)
        elif self.text_type == TextType.TEXT:
            return HtmlNode(value=self.text)
        elif self.text_type == TextType.ITALIC:
            return HtmlNode(tag="i", value=self.text)
        elif self.text_type == TextType.CODE:
            return HtmlNode(tag="code", value=self.text)
        elif self.text_type == TextType.LINK:
            return HtmlNode(tag="a", value=self.text, props={"href": self.url})
        elif self.text_type == TextType.IMAGE:
            return HtmlNode(tag="img", props={"src": self.url, "alt": self.text})
        else:
            raise Exception(f"Unknown text type: {self.text_type}")
