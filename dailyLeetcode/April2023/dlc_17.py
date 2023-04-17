class Solution:
    # https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)

        result = []

        for count in candies:
            result.append(count + extraCandies >= max_val)

        return result
