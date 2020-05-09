class Solution:

    def solve(self, A):
        if A <= 0:
            return []
        res = [[1]]
        if A == 1:
            return res
        res.append([1, 1])
        for num in range(3, A + 1):
            curr = [1]
            for i in range(1, num - 1):
                curr.append(res[num - 2][i - 1] + res[num - 2][i])
            curr.append(1)
            res.append(curr)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve(5))
