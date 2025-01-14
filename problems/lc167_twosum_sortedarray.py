#Variation of the two sum problem

class TwoSumSortedArray:
    def __init__(self):
        pass

    def two_sum(self,arr:list, target):
        """Use a 2 pointer approach"""
        left_ptr = 0
        right_ptr = len(arr)-1
        count=20
        while right_ptr > left_ptr and count>0:
            """If they add up to greater than targer, decrement right pointer. 
            If lesser, increment left pointer. 
            This only works for ascended sorted arrays. """
            count-=1
            if arr[left_ptr]+arr[right_ptr] == target:
                return [left_ptr,right_ptr]
            elif arr[left_ptr]+arr[right_ptr] > target:
                right_ptr-=1
            else:
                left_ptr+=1
        return None
    
def main():
    twosum = TwoSumSortedArray()
    print(twosum.two_sum([1,2,3,4,5],3))

if __name__=='__main__':
    main()
