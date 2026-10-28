class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS,COLS = len(heights), len(heights[0])
        pac,atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            
            # Make sure r, c is not out of bound
            # Our logic would be opposite of what is given in the question:
            # Border -> Inward, value of the cell should grow, then only water can seep from in-->out
            if ((r,c) in visit
            or r < 0 or c < 0
            or r == ROWS or c == COLS
            or heights[r][c] < prevHeight):
                return

            visit.add((r,c))

            # Check in all 4 directions
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        # Col positions that are touching Pacific/Atlantic
        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        # Row positions that are touching Pacific/Atlantic
        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])

        res = []
        # Positions that are touching Pacific && Atlantic
        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) in pac and (r,c) in atl):
                    res.append([r,c])

        return res



        