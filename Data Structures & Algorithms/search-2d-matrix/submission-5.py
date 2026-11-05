class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows ,cols = len(matrix),len(matrix[0])
        
        top,bot = 0,rows - 1

        while top <= bot :
            midRow = (top + bot) // 2

            #[-1] first element
            if target > matrix[midRow][-1]:
                top = midRow + 1

            #[0]last element
            elif target < matrix[midRow][0]:
                bot = midRow -1
            else :
                break
        #If the target isnt in the loop above
        if not (top <= bot):
            return False
        
        #Pick the row with the target that was found 
        midRow = (top + bot) // 2
        l , r = 0, cols - 1

        while l <= r:
            m = (l + r) // 2
            
            if target > matrix[midRow][m]:
                l = m + 1

            elif target < matrix[midRow][m]:
                r = m-1
            else:
                return True
        return False
            