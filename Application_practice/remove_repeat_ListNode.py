class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def creat_linked_list(values):
    """
    根据给定的值列表创建一个单链表。

    Args:
        values (list): 一个包含整数值的列表，用于创建链表。

    Returns:
        ListNode: 链表的头节点（不包括哑节点），其中包含了values中的所有值。
    """
    dummy = ListNode(0)
    cur = dummy
    for num in values:
        node = ListNode(num)
        cur.next = node
        cur = cur.next
    return dummy.next


def remove_repeat_node(head):
    """
    从无序链表中移除与当前节点值相同的后续节点。(腾讯csig后端面试)

    Args:
        head (ListNode): 链表的头节点

    Returns:
        ListNode: 更新后的链表的头节点，其中移除了与当前节点值相同的后续节点

    示例:
    给定链表: 1 -> 3 -> 2 -> 2 -> 3 -> 2 -> 2
    函数将返回: 1 -> 3 -> 2
    """
    # 如果链表为空或只有一个节点，则无需去重
    if head and not head.next:
        return head
    cur = head
    # 只要cur后面还有节点，就继续遍历
    while cur and cur.next:
        runner = cur
        while runner.next:
            # 如果runner的下一个节点的值与curr节点的值相同，说明有重复
            if runner.next.val == cur.val:
                # 移除runner节点,runner位置不动，在下个循环里继续比较，runner.next
                runner.next = runner.next.next
            else:
                runner = runner.next
        cur = cur.next
    return head


def print_linked_list(head):
    """
    打印链表

    Args:
        head (ListNode): 链表的头节点

    Returns:
        ListNode

    示例:
    给定链表: 1 -> 3 -> 2
    函数将返回: 1 -> 3 -> 2
    """
    while head:
        if not head.next:
            print("{}".format(head.val))
        else:
            print("{} -> ".format(head.val), end='')
        head = head.next


if __name__ == '__main__':
    value = [1, 3, 2, 2, 3, 2, 2]
    head = creat_linked_list(value)
    print_linked_list(head)
    print("-------------------------------")
    new_head = remove_repeat_node(head)
    print_linked_list(new_head)




