from collections import defaultdict
from operator import le
from unittest import result


class SlidingWindow:
    def __init__(self, s, k):
        """A class represent all logic in SlidingWindow.

        Args:
            s (str): string input
            k (str): max number of replacement
        """
        self.N = len(s)
        self.s = s
        self.k = k
        # left pointer
        self.left = 0
        # right pointer
        self.right = 0
        # counter
        self.counter = defaultdict(lambda: 0)
        # max character
        self.max_char = None
        self.max_char_freq = 0
        # result
        self.max_length = 0
        # debug
        self.step_counter = 0

    @property
    def length(self):
        return self.right - self.left

    def left_forward(self):
        # 左指针向右移动
        if self.left == self.N - 1:
            raise StopIteration("left doesnot need to forward again")
        # sliding window最左边被排除出范围的char
        char = self.s[self.left]
        self.counter[char] -= 1
        self.max_char, self.max_char_freq = self.get_max_minus(char)
        self.left += 1

    def get_max_minus(self, some=None):
        if not some:
            return self.left[0], 1
        else:
            if self.max_char == some:
                return sorted(self.counter.items(), key=lambda x: x[1], reverse=True)[0]
            else:
                return [self.max_char, self.max_char_freq]

    def get_max_plus(self, some: str):
        assert len(some) == 1, some
        if self.max_char == some:
            return [self.max_char, self.max_char_freq + 1]
        else:
            if self.counter[some] > self.max_char_freq:
                return [some, self.counter[some]]
            else:
                return [self.max_char, self.max_char_freq]

    def right_forward(self):
        # 右指针向右移动
        if self.right == self.N:
            # 此时右指针已经移出s了
            raise StopIteration("right out of bounds")
        # 新进入sliding window的char
        char = self.s[self.right]
        self.counter[char] += 1
        self.max_char, self.max_char_freq = self.get_max_plus(char)
        self.right += 1
        now = self.counter[self.max_char] + self.k
        if now >= self.length:
            self.max_length = max(self.length, self.max_length)

    def step(self):
        self.step_counter += 1
        if self.length > self.max_length:
            self.left_forward()
        else:
            self.right_forward()

    def logic(self):
        while self.left < self.N and self.right <= self.N:
            try:
                self.step()
            except StopIteration as e:
                print(e.args)
                break
            except Exception as e:
                print(e.args)
                raise e
        print("result", self.max_length)
        return self.max_length


class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:

        sw = SlidingWindow(s, k)
        result = sw.logic()
        return result


input1 = [
    (("ABAA", 0), 2),
    (("ABAB", 2), 4),
    (("AABABBA", 1), 4),
]


def test_solution1():
    # ex. 1
    for input, expect in input1:
        res = Solution1().characterReplacement(*input)
        assert res == expect, (res, expect)


class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        # 数据结构
        window = defaultdict(lambda: 0)
        saved_max_length = 0

        # 往右走
        left, right, N, K = 0, 0, len(s), k

        while right <= N - 1:
            c = s[right]
            window[c] += 1
            right += 1
            length = right - left
            max_length = self.max_char(window)
            # 当条件不符合题目时
            while max_length + K < length and left <= N - 1:
                # 不符合条件时，修改left
                c1 = s[left]
                left += 1
                window[c1] -= 1
                # TODO: 为什么这里不用再计算了？
                max_length = self.max_char(window)
                length = right - left
            if max_length + K >= length:
                saved_max_length = max(length, saved_max_length)

        return saved_max_length

    def max_char(self, window: defaultdict):
        return max([i for i in window.items()], key=lambda x: x[1])[1]


def test_solution2():
    for input, expect in input1:
        res = Solution2().characterReplacement(*input)
        assert res == expect, (res, expect)


class Solution3:
    def characterReplacement(self, s: str, k: int) -> int:
        # 跟Solution2比，要快一些，因为max_char不用每步都计算
        chars = {}
        # 快慢指针，window为[left, right)，初始为空，否则max_freq也为0，就是“不一致”
        left, right = 0, 0
        # 长度
        N = len(s)
        # max_freq，指sliding window里面的最大的char的次数
        max_freq = 0
        # 最大长度，结果
        max_length = 0

        def window_is_good():
            return max_freq + k >= right - left

        while left < N:

            # 这个循环就是修改right和chars
            while right < N:
                # 假如此刻window后面一个char计算入window
                char = s[right]
                # 相应window参数变化
                if char not in chars:
                    chars[char] = 1
                else:
                    chars[char] += 1
                max_freq = max(max_freq, chars[char])
                # 计算一下window是否正确
                
                # 往右移进入下一次循环
                right += 1

            
            # 此时right多加了1
            if max_freq + k < right - left + 1:
                max_length = max(max_length, right - left)
            else:
                max_length = max(max_length, right - left + 1)

            # left需要变化
            char = s[left]
            chars[char] -= 1
            left += 1

        return max_length


def test_solution3():
    for input, expect in input1:
        res = Solution3().characterReplacement(*input)
        assert res == expect, (res, expect)