# User function Template for python3

class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.

    def maximumMeetings(self, n, start, end):
        # code here
        meets = [[start[i], end[i]] for i in range(n)]

        meets.sort(key=lambda x: x[1])

        count = 0
        curr_end = 0
        print(meets)
        for i in range(n):
            if curr_end < meets[i][0]:
                curr_end = meets[i][1]
                count += 1

        return count

if __name__ == '__main__':

    sol = Solution()
    n = 8
    start = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
    end = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
    print(sol.maximumMeetings(n, start, end))



# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# if __name__ == '__main__':
#     test_cases = int(input())
#     for cases in range(test_cases):
#         n = int(input())
#         start = list(map(int, input().strip().split()))
#         end = list(map(int, input().strip().split()))
#         ob = Solution()
#         print(ob.maximumMeetings(n, start, end))
# } Driver Code Ends