from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type): #takes in old text node, the string of the character that notes the difference, and the type of text wanted for new place
    new_nodes = [] #empty list to return list of nodes at the end
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node) #if node needs no change, add it and move on
            continue
        split_nodes = [] #empty list to store parts of a node
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0: #checks that everything has been formated correctly
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)): #This is creating the new nodes and their types
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes) #adds list of node sections to existing list of nodes to return
    return new_nodes
