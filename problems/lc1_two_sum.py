# implementing 2 sum

class TwoSum:
    def __init__(self):
        pass

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_dict = {} #create a dictionary to act as a hash map
        for i in range(len(nums)): 
            diff = target-nums[i] #use the difference as a key in the hash map
            if diff in two_dict:
                return([two_dict[diff],i])                
            else:
                two_dict[nums[i]] = i
        return None