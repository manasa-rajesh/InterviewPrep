class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        for ele in prerequisites:
            adj_list[ele[0]].append(ele[1])

        visit = set()
        def dfs(node):
            if node in visit:
                return False
            if len(adj_list[node])==0:
                return True
            visit.add(node)
            for ele in adj_list[node]:
                if not dfs(ele):
                    return False
            visit.remove(node)
            adj_list[node] = []
            return True
                
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        