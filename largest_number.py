class Solution:

    def largestNumber(self, A):
        def mycmp(s1, s2):
            return 1 if s1 + s2 >= s2 + s1 else -1
        A = [str(num) for num in A]
        non_zero = [num for num in A if num != '0']
        if not non_zero:
            return '0'
        A = sorted(A, cmp=mycmp, reverse=True)
        print(A)
        n = len(A)
        ans = ''
        for s in A:
            ans += s
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestNumber([9, 99, 999, 9999, 9998]))
    print(sol.largestNumber([8, 89]))
