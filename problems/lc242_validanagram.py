class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1=list(s)
        temp1.sort()
        temp2=list(t)
        temp2.sort()
        return temp1==temp2
        