class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 想法：以每个index为中心，从这个中心往外找，看是不是palindrome
        longest = 0
        longest_palindrome = ""

        def search_palindrome(i: int, even: bool = False):
            nonlocal longest_palindrome
            nonlocal longest
            offset = 0
            while True:
                left = i - offset
                right = i + offset + int(even)  # 通过这里切换是考虑以i为中心，还是以i和i+1一起为中心
                length = right - left + 1
                if left >= 0 and right < len(s) and s[left] == s[right]:
                    if length > longest:
                        longest_palindrome = s[left : (right + 1)]
                        longest = length
                else:
                    break
                offset += 1

        for i in range(len(s)):
            search_palindrome(i, False)
            search_palindrome(i, True)

        return longest_palindrome


def test_solution():
    examples = [
        ("a", "a"),
        ("babad", ["bab", "aba"]),
        ("cbbd", "bb"),
    ]
    for input, answer in examples:
        res = Solution().longestPalindrome(input)
        result = False
        result = res == answer
        if not result and isinstance(answer, list):
            result = res in answer
        assert result, (input, answer, res)
