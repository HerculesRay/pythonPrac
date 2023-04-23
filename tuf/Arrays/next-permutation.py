class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rev_ind = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                rev_ind = i
                break

        if rev_ind == -1:
            nums.reverse()
            return

        for i in range(n-1, rev_ind, -1):
            if nums[i] > nums[rev_ind]:
                nums[i], nums[rev_ind] = nums[rev_ind], nums[i]
                break

        nums[rev_ind+1:] = reversed(nums[rev_ind+1:])