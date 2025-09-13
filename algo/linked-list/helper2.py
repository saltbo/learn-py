class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(arr, pos=-1):
    """辅助函数：将数组转换为链表"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def find_tail(node):
    dummy = ListNode(0)
    dummy.next = node
    while dummy.next:
        dummy = dummy.next

    return dummy


def find_pos_node(node, pos):
    dummy = ListNode(0)
    dummy.next = node
    count = -1
    while dummy:
        count += 1
        dummy = dummy.next
        if count == pos:
            return dummy
    return None


def link_tail_to_pos(node, pos):
    tail = find_tail(node)
    tail.next = find_pos_node(node, pos)
    return node


def print_linked_list(head):
    """辅助函数：打印链表"""
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))


def create_cycle_linked_list(arr, pos):
    """创建测试用例: arr数组, pos环位置(-1表示无环)"""
    head = create_linked_list(arr)
    if pos >= 0:
        link_tail_to_pos(head, pos)
    return head
