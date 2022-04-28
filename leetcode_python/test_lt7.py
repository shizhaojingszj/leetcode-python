from loguru import logger


class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        meet_sign = False
        digit_start = False # 是否已经见过非零值
        result = []

        min_int = - 2 ** 31
        max_int = 2 ** 31 - 1

        def finalize():
            if not result:
                return 0
            else:
                if sign > 0:
                    return min(int("".join(result)) * sign, max_int) 
                else:
                    return max(int("".join(result)) * sign, min_int)

        for n, i in enumerate(s):
            # 如果是数字
            if i not in "0123456789":
                if not digit_start: 
                    if i == " ":
                        continue
                    elif i in "+-":
                        if meet_sign:
                            return 0
                        meet_sign = True
                        digit_start = True
                        sign = 1 if i == "+" else -1
                    else:
                        return 0
                else:
                    return finalize()
            # 如果不是数字
            else:
                digit_start = True
                if not result and i == "0":
                    continue
                result.append(i)
        return finalize()


def test_solution():
    examples = [
        ("  +  413", 0),
        ("words and 987", 0),
        ("4193 with words", 4193),
        ("   +0 123", 0),
        ("00000-42a1234", 0),
        ("-91283472332", -2147483648),
        ("42", 42),
        ("   -42", -42),
        ("+-12", 0),
    ]
    for input, expect in examples:
        try:
            anw = Solution().myAtoi(input)
        except Exception as e:
            logger.error(e)
            logger.info(input)
            logger.info(expect)
            raise e
        assert anw == expect, (input, expect, anw)
