class Listnode:
    def __init__(self, data=0, next=None):
        self.val=data
        self.next=next

class Solution:

    def insert_at_end(self, head, data):
        new_node = Listnode(data)
        if head is None:
            return new_node
        p = head
        while p.next is not None:
            p = p.next
        p.next = new_node
        return head
    
def print_list(head):
    curr=head
    vals=[]
    while curr:
        vals.append(curr.val)
        curr=curr.next
    print(vals)

if __name__=="__main__":
    sol = Solution()
    head = None
    head = sol.insert_at_end(head, 10)
    head = sol.insert_at_end(head, 20)
    head = sol.insert_at_end(head, 30)
    print_list(head)