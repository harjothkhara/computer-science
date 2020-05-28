# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def addTwoNumbers(self, l1, l2):
        carry = 0
        s = 0  # storing the sum values
        dummy = ListNode()  # start of our result LL
        dummy.next = self.head
        self.head = dummy
        curr = dummy  # to help iterate through result LL

        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            carry = s // 10  # first digit e.g 1 if carry=15
            curr.next = ListNode(s % 10)  # second digit e.g 5 if carry=15
            curr = curr.next

        self.head = dummy.next  # reposition head to ignore dummy node
        return self.head

    # utility function to test
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val),
            temp = temp.next


l1 = Solution()
l2 = Solution()
# CREATE THE FIRST LIST
l1.push(2)
l1.push(4)
l1.push(3)  # current head
print(f"L1 is:")  # 3 -> 4 -> 2
l1.printList()
# CREATE THE SECOND LIST
l2.push(5)
l2.push(6)
l2.push(4)  # current head
print(f"L2 is:")  # 4 -> 6 -> 5
l2.printList()
# ADD THE TWO LISTS AND SEE RESULT
res = Solution()
res.addTwoNumbers(l1.head, l2.head)
print("Resulting List is:")
res.printList()


# Resources:
# https://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
# python_tutor: http://pythontutor.com/live.html#code=%23%20Definition%20for%20singly-linked%20list.%0Aclass%20ListNode%3A%0A%20%20%20%20def%20__init__%28self,%20val%3D0,%20next%3DNone%29%3A%0A%20%20%20%20%20%20%20%20self.val%20%3D%20val%0A%20%20%20%20%20%20%20%20self.next%20%3D%20next%0A%20%20%20%20%20%20%20%20%0Aclass%20Solution%3A%0A%20%20%20%20def%20__init__%28self%29%3A%0A%20%20%20%20%20%20%20%20self.head%20%3D%20None%0A%20%20%20%20%0A%20%20%20%20def%20push%20%28self,%20new_data%29%3A%0A%20%20%20%20%20%20%20%20new_node%20%3D%20ListNode%28new_data%29%0A%20%20%20%20%20%20%20%20new_node.next%20%3D%20self.head%0A%20%20%20%20%20%20%20%20self.head%20%3D%20new_node%0A%20%20%20%20%0A%20%20%20%20def%20addTwoNumbers%28self,%20l1,%20l2%29%3A%0A%20%20%20%20%20%20%20%20carry%20%3D%200%0A%20%20%20%20%20%20%20%20s%20%3D%200%20%23%20storing%20the%20sum%20values%0A%20%20%20%20%20%20%20%20dummy%20%3D%20ListNode%28%29%20%23%20start%20of%20our%20result%20LL%0A%20%20%20%20%20%20%20%20dummy.next%20%3D%20self.head%0A%20%20%20%20%20%20%20%20self.head%20%3D%20dummy%0A%20%20%20%20%20%20%20%20curr%20%3D%20dummy%20%23%20to%20help%20iterate%20through%20result%20LL%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20while%20l1%20or%20l2%20or%20carry%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20s%20%3D%20carry%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20l1%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20s%20%2B%3D%20l1.val%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20l1%20%3D%20l1.next%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20l2%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20s%20%2B%3D%20l2.val%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20l2%20%3D%20l2.next%0A%20%20%20%20%20%20%20%20%20%20%20%20carry%20%3D%20s%20//%2010%20%23%20first%20digit%20e.g%201%20if%20carry%3D15%0A%20%20%20%20%20%20%20%20%20%20%20%20curr.next%20%3D%20ListNode%28s%20%25%2010%29%20%23%20second%20digit%20e.g%205%20if%20carry%3D15%0A%20%20%20%20%20%20%20%20%20%20%20%20curr%20%3D%20curr.next%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20self.head%20%3D%20dummy.next%20%23%20reposition%20head%20to%20ignore%20dummy%20node%0A%20%20%20%20%20%20%20%20return%20self.head%0A%0A%20%20%20%20%23%20utility%20function%20to%20test%0A%20%20%20%20def%20printList%28self%29%3A%0A%20%20%20%20%20%20%20%20temp%20%3D%20self.head%0A%20%20%20%20%20%20%20%20while%28temp%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20print%28temp.val%29,%0A%20%20%20%20%20%20%20%20%20%20%20%20temp%20%3D%20temp.next%0A%0A%0Al1%3DSolution%28%29%0Al2%3DSolution%28%29%0A%23%20CREATE%20THE%20FIRST%20LIST%0Al1.push%282%29%0Al1.push%284%29%0Al1.push%283%29%20%23%20current%20head%0Aprint%28f%22L1%20is%3A%22%29%20%23%203%20-%3E%204%20-%3E%202%0Al1.printList%28%29%0A%23%20CREATE%20THE%20SECOND%20LIST%0Al2.push%285%29%0Al2.push%286%29%0Al2.push%284%29%20%23%20current%20head%0Aprint%28f%22L2%20is%3A%22%29%20%23%204%20-%3E%206%20-%3E%205%0Al2.printList%28%29%0A%23%20ADD%20THE%20TWO%20LISTS%20AND%20SEE%20RESULT%0Ares%3DSolution%28%29%0Ares.addTwoNumbers%28l1.head,%20l2.head%29%0Aprint%28%22Resulting%20List%20is%3A%22%29%0Ares.printList%28%29&cumulative=false&curInstr=120&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
