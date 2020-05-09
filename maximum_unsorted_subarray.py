class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        B = sorted(A)
        if A == B:
            return [-1]
        l, r = -1, -1
        for i, (a, b) in enumerate(zip(A, B)):
            if a != b and l == -1:
                l = i
            elif a != b:
                r = i
        return [l, r]


if __name__ == '__main__':
    sol = Solution()
    print(sol.subUnsort([1, 3, 2, 4, 5]))
