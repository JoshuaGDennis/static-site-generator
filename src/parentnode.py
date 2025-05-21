from htmlnode import HtmlNode


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("must have tag")
        if self.children is None:
            raise ValueError("must have children")
        else:
            string = ""
            tag_text = self.tag

            if self.props is not None:
                tag_text += f"{self.props_to_html()}"

            string = f"<{tag_text}>"

            for child in self.children:
                string += f"{child.to_html()}"

            string += f"</{tag_text}>"

            return string