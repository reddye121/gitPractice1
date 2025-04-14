class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.split()
        print(result[-1])


solution = Solution()
solution.lengthOfLastWord("Hello World")

