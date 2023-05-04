class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = Counter(words)
        words_count = sorted(words_count.items(),key = lambda item:item[0])
        return [item[0] for item in heapq.nlargest(k,words_count,key=lambda item:item[1])]
