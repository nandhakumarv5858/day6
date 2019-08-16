class node:
    def __init__ (self,data):
        self.left=None
        self.right=None
        self.data=data
    def tree(self):
        print(self.data)
        def insert(self.data):
            if data<self.data:
                if data<self.data:
                    if self.left is None:
                        self.left=node(data)
                    else:
                        self.left.insert(data)
                elif data>self.data:
                    if self.right is None:
                        self.right=node(data)
                    else:
                        self.right.insert(data)
            else:
                self.data=data
root=node(12)
root.tree()
