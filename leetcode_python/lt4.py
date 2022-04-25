from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
            
        half = (len(A) + len(B)) // 2
        # quick selectA上的位置：l，r，表示的是A上“节点所在位置的筛选区域”；mid = (r - l) // 2，
        # 对应B上的位置就是：half - mid
        # 需要解决的问题：在[l, r)定义的区间内进行mid位置的查找，可以是binary search
        def quickSelect(l, r):
            mid = l + (r - l) // 2
            B_bound = half - mid - 2
            
            # 这里mid是中点的数，如果r - l为3，那么为1；如果r - l为2，那么也为0；也就是bound在mid后面（也就是说小部分包括mid这个index的数）
            
            # mid这个index的那个数属于“小半部分”
            A_left = A[mid] if mid >= 0 else float("-infinity")
            # 在mid之后的那个数属于“大半部分”
            A_right = A[mid + 1] if mid + 1 >= 0 and mid + 1 < len(A) else float("infinity")
            
            B_left = B[B_bound] if B_bound >= 0 else float("-infinity")
            B_right = B[B_bound + 1] if B_bound + 1 >= 0 and B_bound + 1 < len(B) else float("infinity")
            
            if max(A_left, B_left) <= min(A_right, B_right):
                # 说明找到了正确的bound
                if (len(A) + len(B)) % 2:
                    median = min(A_right, B_right)
                else:
                    median = (max(A_left, B_left) + min(A_right, B_right)) / 2
                return median
            
            else:
                # 说明bound不合适
                if A_left >= B_right:
                    return quickSelect(l, mid)
                else:
                    return quickSelect(mid, r)
        
        # 这里挺重要的，需要搞清楚范围
        return quickSelect(-1, len(A))


def test_solution():
    sl = Solution()
    examples = [
        ([1, 2, 3, 4], [1, 3, 5, 7], 3),
        ([1, 2, 3, 4], [2, 3, 4, 5, 6], 3),
        ([1, 2, 3, 4], [5, 6, 7, 8], 4.5),
        ([1, 2, 3, 4], [5, 6, 7, 8, 9], 5),
        ([5, 6, 7, 8], [1, 2, 3, 4, 5], 5),
    ]
    for nums1, nums2, answer in examples:
        assert sl.findMedianSortedArrays(nums1, nums2) == answer
