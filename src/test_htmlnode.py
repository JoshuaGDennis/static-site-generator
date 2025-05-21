import unittest
from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_single_props_to_html(self):
        node = HtmlNode(props={"stuff": "here"})
        expected = "stuff=\"here\""
        self.assertEqual(node.props_to_html(), expected)

    def test_multiple_props_to_html(self):
        node = HtmlNode(props={"stuff": "here", "stuff2": "here"})
        expected = "stuff=\"here\" stuff2=\"here\""
        self.assertEqual(node.props_to_html(), expected)