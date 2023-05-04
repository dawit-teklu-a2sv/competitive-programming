class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # answer = defaultdict(int)
        # for word in words:
        #     answer[word] += 1
        # answer = list(dict(sorted(answer.items(),key=lambda item: item[1],reverse=True)))
        # return answer[:k]
        words_count = Counter(words)
        words_count = [(word,count) for word,count in words_count.items()]
        words_count.sort(key = lambda i:i[0])
        # heapq.heapify(words_count)
        # print(words_count)
        result = [i[0] for i in heapq.nlargest(k,words_count,key=lambda i:i[1])]
        print(result)
        return result