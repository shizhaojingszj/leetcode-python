"""
1268. Search Suggestions System
-------------------------------------------


Medium


You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

"""
from typing import List


class Node:
    def __init__(self, value: str = None, parent: str = None):
        self.value = value
        self.parent = parent
        self.children = {}

    def add(self, value: str):
        self.children[value] = Node(value, self)


class PrefixTree:

    def construct(self, products: List[str]):
        root = Node()
        for product in products:
            node = root
            for c in product:
                node = node.add(c)




class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        # 数据结构：
        ## 构建prefix tree，还要有顺序

        pass



def test_solution():
    input1 = [
        (
            dict(
                products=["mobile", "mouse", "moneypot", "monitor", "mousepad"],
                searchWord="mouse",
            ),
            [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        ),
        (
            dict(products=["havana"], searchWord="havana"),
            [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
        ),
        (
            dict(
                products=["bags", "baggage", "banner", "box", "cloths"],
                searchWord="bags",
            ),
            [
                ["baggage", "bags", "banner"],
                ["baggage", "bags", "banner"],
                ["baggage", "bags"],
                ["bags"],
            ],
        ),
    ]

    for d, expect in input1:
        assert Solution().suggestedProducts(d["products"], d["searchWord"]) == expect, (
            d,
            expect,
        )
