class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        res_i, res_j, max, sum, start_idx = -1, -1, 0, 0, 0
        for i, c in enumerate(A):
            sum += 1 if c == '0' else -1
            if sum > max:
                res_i = start_idx + 1
                res_j = i + 1
                max = sum
            if sum < 0:
                sum = 0
                start_idx = i + 1
        res = []
        if res_i != -1:
            res = [res_i, res_j]
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.flip('010'))
    print(sol.flip('1101010001'))
