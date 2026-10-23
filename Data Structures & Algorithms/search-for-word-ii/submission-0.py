class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # full word if a word ends here

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, parent):
            ch = board[r][c]
            node = parent.children[ch]

            if node.word:
                res.append(node.word)
                node.word = None          # avoid duplicates

            board[r][c] = '#'             # mark visited
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS
                        and board[nr][nc] in node.children):
                    dfs(nr, nc, node)
            board[r][c] = ch              # backtrack

            # prune: remove exhausted leaf so we never walk it again
            if not node.children:
                del parent.children[ch]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res