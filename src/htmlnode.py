class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # a string
        self.value = value # a string
        self.children = children # a list
        self.props = props # a dictionary


    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
   
    def props_to_html(self):
        if self.props is None:
            return ""
        return_string = ""
        for i in self.props:
            return_string += " " + i + '="' + self.props[i] + '"'
        return return_string
   
    def __repr__(self):
        if self.children is None:
            return f"HTLMNode: {self.tag}, {self.value}, No children, {self.props_to_html()}"
        return f"HTLMNode: {self.tag}, {self.value}, {" ".join(self.children)}, {self.props_to_html()}"
   


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no vlaue")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
   
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
   


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
   
    def to_html(self):
        if self.tag is None:
            return ValueError("invalid HTML: no tag")
        if self.children is None:
            return ValueError("invalid HTML: no children")
        return_string = ""
        for child in self.children:
            return_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{return_string}</{self.tag}>"
   
    def __repr__(self):
        return f"ParentNode({self.tag}, {" ".join(self.children)}, {self.props})"