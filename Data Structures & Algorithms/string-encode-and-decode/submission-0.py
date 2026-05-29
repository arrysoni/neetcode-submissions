class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""
        for i in range(0, len(strs)):
            length = len(strs[i])
            encoded_str += str(length) + "#" + strs[i]
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        arr = []

        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word_start = j + 1
            word_end = word_start + length

            word = s[word_start:word_end]
            arr.append(word)

            i = word_end

        return arr
