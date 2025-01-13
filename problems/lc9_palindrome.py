class IsPalindrome:
    def __init__(self):
        pass

    def is_palindrome_convert_to_str(self, x:int):
        x=str(x)
        return x==x[::-1]