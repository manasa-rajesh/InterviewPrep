class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x,y):
            return ((x**2) + (y**2))**(1/2)
        
        lst = []
        
        for i in range(len(points)):
            lst.append(dist(points[i][0],points[i][1]))
            
        return[x for _, x in sorted(zip(lst, points))][:k]
            
            
        