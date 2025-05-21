class HtmlNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return None

        return " ".join(f"{k}=\"{v}\"" for k, v in self.props.items())

    def __repr__(self):
        string = ""
        string += f"tag=\"{self.tag}\" \n"
        string += f"value=\"{self.value}\" \n"

        if self.children is not None and len(self.children) > 0:
            string += f"--children--\n"

            for child in self.children:
                string += f"{child} \n"

        if self.props is not None and len(self.props) > 0:
            string += f"--props--\n"
            for prop in self.props:
                string += f"{prop}={self.props[prop]} \n"

        return string




# Add a .to_html() method that renders a leaf node as an HTML string (by returning a string).
# If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
# If there is no tag (e.g. it's None), the value should be returned as raw text.
# Otherwise, it should render an HTML tag. For example, these leaf nodes:
# LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
# "<a href="https://www.google.com">Click me!</a>"