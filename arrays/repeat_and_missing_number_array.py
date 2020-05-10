class Solution:

    def func(self, A):
        n = len(A)
        a = -1
        m = {}
        for num in A:
            if not m.get(num, 0):
                m[num] = 1
            else:
                a = num
                break
        b = n * (n + 1) // 2 + a - sum(A)
        return [a, b]


if __name__ == '__main__':
    sol = Solution()
    print(sol.func([1, 2, 3, 5, 5]))
