class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def insert_at_begin(self, head, data):
        new_node = ListNode(data)
        new_node.next = head
        return new_node


def print_list(head):
    cur = head
    vals = []
    while cur:
        vals.append(cur.data)
        cur = cur.next
    print(vals)


if __name__ == "__main__":
    sol = Solution()
    head = None
    head = sol.insert_at_begin(head, 10)
    head = sol.insert_at_begin(head, 20)
    head = sol.insert_at_begin(head, 30)
    print_list(head)
