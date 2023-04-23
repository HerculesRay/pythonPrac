# User function Template for python3

class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform(self, n, arr, dep):
        # code here
        arr.sort()
        dep.sort()

        arrp = 1
        depp = 0
        curr_ct = 1
        max_ct = 1

        while arrp < n:
            if arr[arrp] > dep[depp]:
                depp += 1
            arrp += 1
            curr_ct = arrp - depp
            max_ct = max(max_ct, curr_ct)

        return max_ct


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(n, arrival, departure))
# } Driver Code Ends