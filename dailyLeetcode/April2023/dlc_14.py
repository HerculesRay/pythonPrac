class Solution:
    # Problem link - https://leetcode.com/problems/longest-palindromic-subsequence
    def longestCommonSeq(self, ostr, rstr):

        m = len(ostr) + 1
        n = len(rstr) + 1

        dp = []

        for i in range(m):
            dp.append([0] * n)


        for i in range(1, m):
            for j in range(1, n):
                beval = max(dp[i - 1][j], dp[i][j - 1])
                dival = dp[i - 1][j - 1]
                if rstr[i - 1] == ostr[j - 1]:
                    dival += 1
                dp[i][j] = max(dival, beval)
        return dp[m - 1][n - 1]

    def longestPalindromeSubseq(self, s: str) -> int:

        return self.longestCommonSeq(s, s[::-1])

sol = Solution()

print(sol.longestPalindromeSubseq("bbbab"))

