#Solution for majority element

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        highest_count=0
        highest_index=0
        for i in range(len(nums)):
            thecount = nums.count(nums[i])      
            if thecount>highest_count:
                highest_count=thecount
                highest_index=i
        return nums[highest_index]


if __name__=='__main__':
    s=Solution()
    print(s.majorityElement([3,2,2,2]))