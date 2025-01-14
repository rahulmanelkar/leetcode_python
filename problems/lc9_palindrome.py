class IsPalindrome:
    def __init__(self):
        pass

    def is_palindrome_convert_to_str(self, x:int):
        x=str(x)
        return x==x[::-1]

def main():
    palindrome = IsPalindrome()
    print(palindrome.is_palindrome_convert_to_str(42))

if __name__ == '__main__':
    main()