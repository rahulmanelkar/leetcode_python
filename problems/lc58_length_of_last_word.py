#Length of last word. Using python paradigm and then generic
class LC58:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
if __name__ == '__main__':
    lc = LC58()
    print(lc.lengthOfLastWord("Hello World"))