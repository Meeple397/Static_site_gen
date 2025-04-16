from textnode import TextNode, TextType


def main():
    node = TextNode("This is a duck", TextType.LINK, "https://upload.wikimedia.org/wikipedia/commons/b/bf/Bucephala-albeola-010.jpg")
    print(node)


main()