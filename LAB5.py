# LAB 5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(9)
        >>> x.insert(4)
        >>> x._numLeaves()
        1
        >>> x.insert(11)
        >>> x.insert(2)
        >>> len(x)
        4
        >>> x.insert(5)
        >>> x.insert(10)
        >>> x._numLeaves()
        3
        >>> x.insert(9.5)
        >>> x.insert(7)
        >>> len(x)
        8
        >>> x.getMin
        Node(2)
        >>> x.getMax
        Node(11)
        >>> 67 in x
        False
        >>> 9.5 in x
        True
        >>> x.isEmpty()
        False
        >>> x.getHeight(x.root)   # Height of the tree
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.getHeight(x.root.right.left)
        1
        >>> x.printInorder
        2 : 4 : 5 : 7 : 9 : 9.5 : 10 : 11 : 
    '''
    def __init__(self):
        self.root = None


    def insert(self, value):
        if self.root is None:
            self.root=Node(value)
        else:
            self._insert(self.root, value)


    def _insert(self, node, value):
        if(value<node.value):
            if(node.left==None):
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:   
            if(node.right==None):
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    @property
    def printInorder(self):
        if self.isEmpty(): 
            return None
        else:
            self._inorderHelper(self.root)
        
    def _inorderHelper(self, node):
        if node is not None:
            self._inorderHelper(node.left) 
            print(node.value, end=' : ') 
            self._inorderHelper(node.right)  


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.root is None
        pass
       
    def __len__(self):
        return self._lenHelper(self.root)

    def _lenHelper(self, node):
        # YOUR CODE STARTS HERE
        if node is None:
            return 0
        return self._lenHelper(node.left) + self._lenHelper(node.right) + 1
        pass


    def _numLeaves(self):
        return self._numLeavesHelper(self.root)


    def _numLeavesHelper(self, node):
        # YOUR CODE STARTS HERE
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return self._numLeavesHelper(node.left) + self._numLeavesHelper(node.right)
        pass



    @property
    def getMin(self): 
        # YOUR CODE STARTS HERE
        temp = self.root
        while not temp.left is None:
            temp = temp.left
        return temp
        pass


    @property
    def getMax(self): 
        # YOUR CODE STARTS HERE
        temp = self.root
        while not temp.right is None:
            temp = temp.right
        return temp
        pass

    def __contains__(self, value):
        # YOUR CODE STARTS HERE
        temp = self.root
        while not temp is None:
            if temp.value == value:
                return True
            elif temp.value > value:
                temp = temp.left
            else:
                temp = temp.right
        return False
        pass



    def getHeight(self, node):
        # YOUR CODE STARTS HERE
        if self.root is None or node is None:
            return 0
        elif node.left is None and node.right is None:
            return 0
        if self.getHeight(node.left) > self.getHeight(node.right):
            return self.getHeight(node.left) + 1
        else:
            return self.getHeight(node.right) + 1
        pass


if __name__=='__main__':
    import doctest
    doctest.testmod()
