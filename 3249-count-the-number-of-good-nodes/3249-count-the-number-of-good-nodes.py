from collections import defaultdict

class Solution:
    def dfs(self, node, parent, g, sb, ans):
        sb[node] = 1
        isGoodNode = True
        f = -1
        for c in g[node]:
            if c != parent:
                cs = self.dfs(c, node, g, sb, ans)
                if f == -1:
                    f = cs
                elif f != cs:
                    isGoodNode = False
                sb[node] += sb[c]
        if isGoodNode:
            ans[0] += 1
        return sb[node]

    def countGoodNodes(self, edges):
        g = defaultdict(list)
        n = len(edges) + 1
        for edge in edges:
            u, v = edge
            g[u].append(v)
            g[v].append(u)

        sb = {}
        ans = [0]
        self.dfs(0, -1, g, sb, ans)

        return ans[0]

