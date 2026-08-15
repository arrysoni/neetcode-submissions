class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        # Step 1: Count each number
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Step 2: Create buckets
        freq = [[] for i in range(len(nums) + 1)]

        # Step 3: Put numbers into buckets
        for num in count:
            frequency = count[num]
            freq[frequency].append(num)

        # Step 4: Go backwards
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result

