from src.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    new_nodes = []

    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            new_nodes.append(n)
        else:
            open_index = n.text.find(delimiter)
            close_index = n.text.find(delimiter, open_index + 1)

            if open_index == -1:
                new_nodes.append(n)
            elif close_index == -1:
                raise ValueError("invalid value")
            else:
                before = n.text[0:open_index]
                middle = n.text[open_index + 1:close_index]
                after = n.text[close_index:]

                new_nodes.append(TextNode(before, TextType.TEXT))
                new_nodes.append(TextNode(middle, text_type))
                new_nodes.append(TextNode(after, TextType.TEXT))

    return new_nodes