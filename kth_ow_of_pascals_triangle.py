class Solution:

    def getRow(self, A):
        prev, curr = [1], [1, 1]
        if A < 0:
            return []
        if A == 0:
            return prev
        if A == 1:
            return curr
        for num in range(2, A + 1):
            prev = curr
            curr = [1]
            for i in range(1, num):
                curr.append(prev[i - 1] + prev[i])
            curr.append(1)
        return curr

    def alternate(self, A):
        val = 1
        res = []
        for i in range(0, A + 1):
            res.append(val)
            val = val * (A - i) // (i + 1)
        return res


if __name__ == '__main__':
    sol = Solution()
    # print(sol.getRow(4))
    print(sol.alternate(4))
