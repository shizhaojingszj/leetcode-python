class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 想法：以每个index为中心，从这个中心往外找，看是不是palindrome
        longest = 0
        longest_palindrome = ''
        def search_palindrome(i: int):
            offset = 0
            while True:
                left = i - offset
                right = i + offset + 1
                length = right - left + 1
                if left > 0 and right < len(s) and s[left] == s[right]:
                    if length > longest:
                        longest_palindrome = s[left, right]
                        longest = length
                    continue
                else:
                    break

                offset += 1
        
        for i in range(len(s)):
            search_palindrome(i)
        
        return longest_palindrome


def test_solution():
    examples = [
        ("babad", "bab"),
        ("cbbd", "bb"),
    ]
    for input, answer in examples:
        assert Solution().longestPalindrome(input) == answer