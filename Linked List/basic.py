
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Signly_Linked_List(object):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert_head(self, data):
        node = Node(data)
        if self.head != None:
            node.next = self.head
        self.head = node

    def insert_tail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next!= None:
                temp = temp.next
            temp.next = node


    def search(self, data):
        if self.head is None:
            return "Not found"
        else:
            temp = self.head
            index = 0
            while temp!=None:
                if temp.data == data:
                    return index
                temp = temp.next
                index += 1
            return "Not found"

    def delete(self, data):
        if self.search(data) == "Not found":
            return "no this data"
        elif self.head.data == data:
            self.head = self.head.next
        else:
            temp = self.head
            pre_temp = None
            while temp!= None:
                if temp.data == data:
                    pre_temp.next = temp.next
                pre_temp = temp
                temp = temp.next

    def delete_index(self, index):
        if index < 0:
            return "error"
        elif index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            pre_temp = None
            while index > 0:
                if temp.next == None:  #超出链表范围
                    return  "error"
                pre_temp = temp
                temp = temp.next
                index -= 1
            pre_temp.next = temp.next



if __name__ == '__main__':
    linklist = Signly_Linked_List()
    linklist.insert_tail(55)
    linklist.insert_tail(58)
    linklist.insert_tail(66)
    print(linklist.search(58))
    print(linklist.delete_index(2))
    # linklist.insert_tail(78)
    pass






