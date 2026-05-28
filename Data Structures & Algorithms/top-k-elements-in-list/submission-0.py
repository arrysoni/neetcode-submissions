class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        output = []

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        for num in sorted_freq:
            if len(output) == k:
                break
            output.append(num)

        return output

        

        