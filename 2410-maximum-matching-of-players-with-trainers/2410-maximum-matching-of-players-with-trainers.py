class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        n = len(players)
        m = len(trainers)
        left=right=0
        while left < n and right < m:
            if players[left] <= trainers[right]:
                print(players[left],trainers[right])
                count += 1
                left += 1
                right += 1
            else:
                right += 1
        return count
        
        