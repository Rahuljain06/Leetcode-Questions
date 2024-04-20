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
                    visited[r]= all(dfs(i) for i in d[r]) 
            return visited[r]
            
            
                
        for i in recipes:
            if dfs(i):
                res.append(i)
        return res
    
#     def dfs(r):
#             if r not in can_make:
#                 can_make[r] = False
#                 if r in graph:
#                     can_make[r] = all([dfs(i) for i in graph[r]])
#             return can_make[r]
        
#         can_make = {s: True for s in supplies}
#         graph = {r : ing for r, ing in zip(recipes, ingredients)}
#         return [r for r in recipes if dfs(r)]
