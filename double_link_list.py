import single_link_list


class Node(object):
    def __init__(self, item):
        """节点"""
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(single_link_list.SingleLinkList):
    """双链表"""
    def __init__(self):
        super().__init__()

    def add(self, item):
        """链表头部添加元素 头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加元素 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    cur.prev.next=cur.next
                    if cur.next:
                        cur.next.prev=cur.prev
                break
            else:
                cur = cur.next


if __name__ == '__main__':
    dll = DoubleLinkList()
    print(dll.is_empty())
    dll.append(1)
    dll.append(2)
    dll.append(3)
    print(dll.travel())
    print(dll.is_empty())
