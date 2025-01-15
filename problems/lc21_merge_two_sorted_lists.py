#Solution for merging 2 sorted lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeTwoLists:
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        i=0
        j=0
        listr=[]
        while(i<len(list1) and j<len(list2)):
            if list1[i]<=list2[j]:
                listr.append(list1[i])
                i+=1
            else:
                listr.append(list2[j])
                j+=1
        listr.extend(list1[i:])
        listr.extend(list2[j:])

        return listr

    def mergeTwoLinkedLists(self, list1, list2):
        #2 linked lists are passed in instead. The nodes are mentioned above. 
        pass

def build_linked_list(elements):
    head = ListNode(val=elements[0],next=None)
    pointer=head
    for elem in elements[1:]:
        #print(elem)
        temp_node = ListNode(elem,next=None)
        pointer.next = temp_node
        pointer = pointer.next        

    return head

def print_linked_list(head_node):
    pointer = head_node
    while pointer:
        print(f'{pointer.val}-->',end="")
        pointer=pointer.next


if __name__=='__main__':
    merge = MergeTwoLists()
    my_list = merge.mergeTwoLists([1,2,3,10],[1,6,7])
    #print(my_list)

    my_ll = build_linked_list([34,56,78,99])
    print_linked_list(my_ll)