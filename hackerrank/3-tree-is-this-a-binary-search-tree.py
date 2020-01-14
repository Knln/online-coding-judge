""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
smallNumber = 0

def checkBST(root):
    list = []
    changeList(root, list)
    for index, element in enumerate(list):
        if (index == 0):
            pass
        elif(list[index-1] >= list[index]):
            return False
    
    return True

def changeList(tree, list):
    if not tree:
        return
    
    changeList(tree.left, list) 
    list.append(tree.data)
    changeList(tree.right, list)
