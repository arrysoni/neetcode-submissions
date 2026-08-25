class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_strs = ""

        for wrd in strs:
            length = len(wrd)
            encoded_strs += str(length) + "#" + wrd

        return encoded_strs

    def decode(self, s: str) -> List[str]:

        decoded_strs = []

        while s:

            # Find where the length ends
            i = s.index("#")

            # Get the length
            num = int(s[:i])

            # Get the word
            wrd = s[i + 1 : i + 1 + num]

            decoded_strs.append(wrd)

            # Remove what we just decoded
            s = s[i + 1 + num:]

        return decoded_strs