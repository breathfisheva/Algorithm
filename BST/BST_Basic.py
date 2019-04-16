
class BSTree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if data < self.data:
            if self.left == None:
                self.left = BSTree(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right == None:
                self.right = BSTree(data)
            else:
                self.right.insert(data)

    def findMax(self):
        if self.right:
            return self.right.findMax() #注意这里要加return，否则只有最后一个层级有return，之前的层级没有return，这样就没有返回值了
        else:
            return self.data


    def delete(self, data):
        if data < self.data:
            self.left = self.left.delete(data)
            return self
        elif data > self.data:
            self.right = self.right.delete(data)
            return self
        else:
            if self.left and self.right:
                del_node = self.right.findMax()
                self.data = del_node.data
                del_node = None
                return self
            elif self.left:
                self = self.left
                return self
            elif self.right:
                self = self.right
                return self
            else:
                self = None
                return self

    def preorder(self):
        '''打印二叉树(先序)'''
        if self == None:
            return
        print(self.data, end=' ')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def midorder(self):
        '''打印二叉树(中序)'''
        if self == None:
            return
        if self.left:
            self.left.midorder()
        print(self.data, end=' ')
        if self.right:
            self.right.midorder()

    def backorder(self):
        '''打印二叉树(后序)'''
        if self == None:
            return
        if self.left:
            self.left.backorder()
        if self.right:
            self.right.backorder()
        print(self.data, end=' ')

    def print_level(self):
        '''打印二叉树，根据层级'''
        current_node = []
        next_node = []

        current_node.append(self)

        while current_node:
            for node in current_node:
                print(node.data, end='') #end='' 代表不分行
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            current_node = next_node
            next_node = []
            print('')


if __name__ == '__main__':
    t = BSTree(7)
    t.insert(3)
    t.insert(4)
    t.insert(8)
    t.insert(1)
    t.insert(10)
    t.insert(5)
    # t.preorder()
    # t.backorder()
    #
    # t.print_level()
    print(t.findMax())
    t.delete(8)
    print('   ')
    t.print_level()