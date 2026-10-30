class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True

        # Create adj. list node:[neighbour]
        adj = {i:[] for i in range(n)}

        # Fill in the adj. list
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):

            if i in visit:
                return False

            visit.add(i)

            # For neighbours of i 
            for j in adj[i]:
                if j == prev: # The node has no more neighnours except prev
                    continue

                if not dfs(j,i):
                    return False
                
            return True
        
        # Conditions for valid tree
        return dfs(0, -1) and n == len(visit)

        
        