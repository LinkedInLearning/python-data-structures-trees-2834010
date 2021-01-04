class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def traversePreorder(self):
        print(self.data)
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.data)
        if self.right:
            self.right.traverseInorder()

    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder()
        print(self.data)

    def search(self, target):
        if self.data == target:
            print("Found it!")
            return self
        
        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print("Value is not in tree")


    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        
        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes

    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h 
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)

    def add(self, data):
        if data == self.data:
            # Binary search tree does not contain duplicates
            return
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                return
            else:
                self.left.add(data)                
        
        if data > self.data:
            if self.right is None:
                self.right = Node(data)
                return
            else:
                self.right.add(data)

    def findMin(self):
        if self.left:
            return self.left.findMin()
        return self

    def delete(self, target):
        if self.data == target:
            if self.right and self.left:
                minimumValue = self.right.findMin()
                self.data = minimumValue.data
                self.right = self.right.delete(minimumValue.data)
                return self
            else: 
                return self.right or self.left
        
        if self.right and target > self.data:
                self.right = self.right.delete(target)

        if self.left and target < self.data:
                self.left = self.left.delete(target)
        return self

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_'+(' '*spacing)
        spacing = spacing-len(str(n))+1
        return str(n)+(' '*spacing)

    def print(self, label=''):
        print(self.name+' '+label)
        height = self.root.height()
        spacing = 3
        width = int((2**height-1) * (spacing+1) + 1)
        # Root offset
        offset = int((width-1)/2)
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1)  + (' '*(spacing+2)).join(['/' + (' '*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.root.getNodesAtDepth(depth, [])
            print((' '*offset)+''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')

    def traverseInorder(self):
        self.root.traverseInorder()

    def traversePreorder(self):
        self.root.traversePreorder()

    def traversePostorder(self):
        self.root.traversePostorder()

    def search(self, target):
        return self.root.search(target)

    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)

    def height(self):
        return self.root.height()

    def add(self):
        self.root.add()

    def delete(self, target):
        self.root = self.root.delete(target)


tree = Tree(Node(50))
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.right.left = Node(67)
tree.root.right.right = Node(100)
tree.root.right.right.right = Node(120)
tree.root.right.right.left = Node(80)
tree.root.right.right.left.right = Node(92)

tree.print()

tree.delete(75)
tree.delete(50)
tree.print()