class Solution:
    def canMeasureWater(
        self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int
    ) -> bool:
        j1, j2, t = jug1Capacity, jug2Capacity, targetCapacity

        if j1 == t or j2 == t or j1 + j2 == t:
            return True

        if j1 + j2 < t:
            return False

        # 保证j1 < j2
        if j1 > j2:
            j1, j2 = j2, j1

        # helper
        def ok(j2_state):
            if 0 <= j2_state <= j2 and j2_state not in seen:
                return True

        # 高级逻辑……
        stack = [0]  # 永远是当前j2的水量
        seen = set()
        while stack:
            # j2的水量
            state = stack.pop()

            if state == t or state + j1 == t:
                return True

            seen.add(state)

            next_states = [
                state + j1,  # 1. 当前j2可以加上j1总量
                state - j1,  # 2. 当前j2可以倒给j1，还有剩
                j1 - (j2 - state),  # 3. 1的情况引申：j2不能加上完整的j1了，此时j1剩下的量，属于前面没见过的，需要见一见
                j2 - (j1 - state),  # 4. 2的情况引申：j2倒给j1，没剩了，还不够j1完整，此时j1的剩余量没见过；
            ]

            for s in next_states:
                if ok(s):
                    stack.append(s)

        return False


def test_solution():
    input1 = [
        (dict(jug1Capacity=3, jug2Capacity=5, targetCapacity=4), True),
    ]

    for input, expect in input1:
        assert Solution().canMeasureWater(**input) == expect, (input, expect)
