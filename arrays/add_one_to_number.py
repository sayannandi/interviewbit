class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        print(A)
        remove = 0
        for num in A:
            print(num)
            if num == 0:
                remove += 1
            else:
                break
        for i in range(remove):
            A.pop(0)
        n = len(A)
        print(A)
        carry_over = 1
        for i in range(n - 1, -1, -1):
            A[i] += carry_over
            carry_over = 0
            if A[i] > 9:
                carry_over += A[i] // 10
                A[i] %= 10
            else:
                break
        while carry_over:
            A.insert(0, carry_over % 10)
            carry_over //= 10
        return A


if __name__ == '__main__':
    sol = Solution()
    print(sol.plusOne([0, 6, 0, 6, 4, 8, 8, 1]))
