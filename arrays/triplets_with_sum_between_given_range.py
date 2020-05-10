class Solution:

    def solve(self, A):
        A.sort()
        n = len(A)
        print(A)
        i, j = 0, n - 1
        while i + 1 < j:
            s = (float)(A[i]) + (float)(A[i + 1]) + (float)(A[j])
            print(s)
            if s <= 1:
                i += 1
            elif 2 <= s:
                j -= 1
            else:
                return 1
        return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.solve(["0.297657", "0.420048", "0.053365", "0.437979", "0.375614", "0.264731", "0.060393", "0.197118",
                     "0.203301", "0.128168"]))
