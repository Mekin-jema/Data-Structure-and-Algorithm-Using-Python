class TreeNode:
    def __init__(self,value,children=[]):
        self.value=value
        self.children=children
    def __str__(self,level=0):
        ret=" "*level+ str(self.value)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret
    
    def addChild(self,treeNode):
        self.children.append(treeNode)