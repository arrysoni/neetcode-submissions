class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        used = set()

        for i in range(0, len(strs)):

            if i in used:
                continue

            sublist = [strs[i]]
            used.add(i)

            for j in range(i+1, len(strs)):
                if (sorted(strs[i]) == sorted(strs[j])):
                    sublist.append(strs[j])
                    used.add(j)
                
            output.append(sublist)
        
        return output

        