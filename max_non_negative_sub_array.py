class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        res, curr, curr_sum, max_sum = [], [], 0, 0
        for num in A:
            if num < 0:
                if curr_sum > max_sum or (curr_sum == max_sum and len(curr) > len(res)):
                    res = curr
                    max_sum = curr_sum
                curr_sum = 0
                curr = []
            else:
                curr_sum += num
                curr.append(num)

        if curr_sum > max_sum or (curr_sum == max_sum and len(curr) > len(res)):
            res = curr
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxset([1, 2, 5, -7, 2, 3]))
    print(sol.maxset([10, -1, 2, 3, -4, 100]))