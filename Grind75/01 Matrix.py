class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        lst = []
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    lst.append([i,j])
                else:
                    mat[i][j] = '*'
                    
        for row,col in lst:
            for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                nr = row+dx
                nc = col+dy
                if 0<=nr<rows and 0<=nc<cols and mat[nr][nc]=='*':
                    mat[nr][nc] = mat[row][col] + 1
                    lst.append([nr,nc])
                    
                
                
        return mat
                    
        