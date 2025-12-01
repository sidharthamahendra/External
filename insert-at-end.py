class Listnode:
    def __init__(self, data=0, next=None):
        self.val=data
        self.next=next

class Solution:
    def __init__(self,head=None):
        self.head=head
        
    def insert_at_end(self, data):
        new_node=Listnode(data)
        if self.head==None:
            self.head=new_node
        else:
            p=self.head
            while p.next != None:
                p=p.next
            p.next=new_node
            
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