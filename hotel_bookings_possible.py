class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        events = []
        for a, d in zip(arrive, depart):
            events.append((a, 1))
            events.append((d, -1))
        events.sort()
        occupied_rooms = 0
        print(events)
        for (_, status) in events:
            occupied_rooms += status
            if occupied_rooms > K:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.hotel([1, 3, 5], [2, 6, 8], 1))
