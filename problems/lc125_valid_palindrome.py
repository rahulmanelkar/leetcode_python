#valid palindrome given contraints

import re
def remove_alphanumeric(string):
    return re.sub(r'[^a-zA-Z0-9]', '', string)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=remove_alphanumeric(s)
        s=s.lower().replace(" ","")
        return s==s[::-1]
        