class Solution:
    def countGoodNodes(self, e: List[List[int]]) -> int:
        t = defaultdict(list)
        n=len(e)+1
        for u, v in e:
            t[u].append(v)
            t[v].append(u)
        print(t)
        sz = [1] * n
        cnt = 0
        def dfs(nd, p):
            nonlocal cnt
            c = []
            for nbr in t[nd]:
                if nbr == p:
                    continue
                sz[nd] += dfs(nbr, nd)
                c.append(sz[nbr])
            if len(set(c)) <= 1:
                cnt += 1
            return sz[nd]
        dfs(0, -1)
        return cnt