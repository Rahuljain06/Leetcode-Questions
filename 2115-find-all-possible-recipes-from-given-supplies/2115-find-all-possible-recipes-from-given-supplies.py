class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        d=defaultdict(list)
        for i in range(len(recipes)):
            d[recipes[i]].extend(ingredients[i])
            
        res=[]
        visited={}
        for s in supplies:
            visited[s]=True
            
        def dfs(r):
            if r not in visited:
                visited[r]=False
                if r in d:
                    all_children_visited = True
                    for i in d[r]:
                        if not dfs(i):
                            all_children_visited = False
                            break
                    visited[r] = all_children_visited
                    # visited[r]= all(dfs(i) for i in d[r]) 
            return visited[r]

        for i in recipes:
            if dfs(i):
                res.append(i)
        return res