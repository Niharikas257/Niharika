class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

       
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  
            (0, -1),        (0, 1),      
            (1, -1), (1, 0), (1, 1)      
        ]

        
        def count_live_neighbors(r, c):
            live_neighbors = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                    live_neighbors += 1
            return live_neighbors

        
        for r in range(rows):
            for c in range(cols):
                
                live_neighbors = count_live_neighbors(r, c)

                
                if board[r][c] == 1:  # Current cell is live
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = -1  
                else:  
                    if live_neighbors == 3:
                        board[r][c] = 2  

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == -1:
                    board[r][c] = 0  
                elif board[r][c] == 2:
                    board[r][c] = 1  


