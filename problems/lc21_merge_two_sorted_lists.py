#Solution for merging 2 sorted lists

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

if __name__=='__main__':
    merge = MergeTwoLists()
    my_list = merge.mergeTwoLists([1,2,3,10],[1,6,7])
    print(my_list)