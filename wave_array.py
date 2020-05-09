class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        for i in range(0, len(A) - 1, 2):
            t = A[i]
            A[i] = A[i + 1]
            A[i + 1] = t
            i += 1
        return A


if __name__ == '__main__':
    sol = Solution()
    print(sol.wave([6, 17, 15, 13]))
    print(sol.wave([1, 2, 3]))
    print(sol.wave([1, 2, 3, 4]))
