#Working on lc28

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)==1:
            if needle==haystack:
                return 0
            else:
                return -1
            
        if len(needle)==1 or len(needle)==len(haystack):
             cmp = len(haystack)
        else:
             cmp = len(haystack)-len(needle)

        for i in range(cmp+1):
                if needle == haystack[i:i+len(needle)]:
                    return i
        return -1
    
if __name__=='__main__':
    s = Solution()
    hay = "mississippi"
    nee = "ppi"
    print(s.strStr(hay,nee))