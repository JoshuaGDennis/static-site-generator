from types import NoneType

from htmlnode import  HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value cannot be None")
        elif self.tag is None:
            return self.value

        tag_text = self.tag

        if self.props is not None:
            tag_text += f" {self.props_to_html()}"

        return f"<{tag_text}>{self.value}</{self.tag}>"