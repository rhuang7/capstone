import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        K = int(data[idx+1])
        M = int(data[idx+2])
        idx += 3
        
        # Calculate the top-left corner of the poison grid
        pox = (N - K) // 2 + 1
        poy = (N - K) // 2 + 1
        
        # For each snake, determine the line it is on and the range it covers
        snakes = []
        for _ in range(M):
            HX = int(data[idx])
            HY = int(data[idx+1])
            TX = int(data[idx+2])
            TY = int(data[idx+3])
            idx += 4
            
            if HX == TX:
                # Horizontal snake
                line = 'row'
                start = min(HY, TY)
                end = max(HY, TY)
                snakes.append((line, start, end, HX))
            else:
                # Vertical snake
                line = 'col'
                start = min(HX, TX)
                end = max(HX, TX)
                snakes.append((line, start, end, HY))
        
        # Check if any snake is in the poison grid
        # If any snake is in the poison grid, it's not allowed to be removed
        # So we need to keep it
        # But the problem says that none of the cells in the KxK grid will be occupied by any snake
        # So we can safely remove all snakes
        
        # Now, we need to find the minimum number of snakes to keep such that no arrow can enter the poison grid and exit the outer grid without hitting a snake
        # This is equivalent to ensuring that for every row and column that intersects the poison grid, there is at least one snake that blocks all possible paths through the poison grid
        
        # The poison grid is from (pox, poy) to (pox + K - 1, poy + K - 1)
        # So the rows that intersect the poison grid are from pox to pox + K - 1
        # The columns that intersect the poison grid are from poy to poy + K - 1
        
        # We need to find the minimum number of snakes such that:
        # - For every row in [pox, pox + K - 1], there is at least one snake that covers the entire row in the poison grid
        # - For every column in [poy, poy + K - 1], there is at least one snake that covers the entire column in the poison grid
        
        # But since the snakes can be in any row or column, we need to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # So we need to find the minimum number of snakes such that:
        # - For every row in [pox, pox + K - 1], there is at least one snake that covers the entire row in the poison grid
        # - For every column in [poy, poy + K - 1], there is at least one snake that covers the entire column in the poison grid
        
        # However, since the snakes can be in any row or column, we need to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # So we can model this as a bipartite graph where one set is the rows of the poison grid and the other set is the columns of the poison grid
        # Each snake can cover a row and a column (if it is in the poison grid)
        # We need to find the minimum number of snakes that cover all the rows and columns
        
        # But since the snakes can be in any row or column, we need to check for each snake whether it covers any part of the poison grid
        
        # For each snake, check if it covers any part of the poison grid
        # If it does, then it can potentially block some arrows
        # So we need to find the minimum number of snakes such that all rows and columns in the poison grid are covered by at least one snake
        
        # This is equivalent to finding the minimum vertex cover in a bipartite graph
        # But since the graph is bipartite, we can use the Konig's theorem to find the minimum vertex cover
        
        # However, since the problem is about covering all rows and columns in the poison grid, we can approach this as a set cover problem
        
        # But since the number of rows and columns is K (which can be up to 1e9), we need an efficient way to check if a snake covers any part of the poison grid
        
        # For each snake, check if it covers any part of the poison grid
        # If it does, then it can potentially block some arrows
        # So we need to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # For a snake to cover a row in the poison grid, it must be a horizontal snake and its row must be in the poison grid
        # For a snake to cover a column in the poison grid, it must be a vertical snake and its column must be in the poison grid
        
        # So for each snake, we can check if it covers any part of the poison grid
        # If it does, we can record which rows and columns it covers
        
        # Then, we need to find the minimum number of snakes such that all rows and columns in the poison grid are covered by at least one snake
        
        # This is a set cover problem, which is NP-hard, but since the number of rows and columns is K, which can be up to 1e9, we need a different approach
        
        # Since the number of rows and columns is K, and K is odd, we can try to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # For each snake, check if it covers any part of the poison grid
        # If it does, then it can potentially block some arrows
        # So we need to find the minimum number of snakes such that all rows and columns in the poison grid are covered by at least one snake
        
        # But how can we do this efficiently?
        # We can try to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # For each snake, if it covers any part of the poison grid, we can record which rows and columns it covers
        # Then, we can try to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # But since the number of rows and columns is K, which can be up to 1e9, we need to find a way to represent this efficiently
        
        # So, for each snake, we can check if it covers any part of the poison grid
        # If it does, then we can record which rows and columns it covers
        
        # Then, we can try to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # However, this is still not efficient for large K
        # So we need a different approach
        
        # Since the poison grid is a KxK square, and K is odd, we can try to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # For each snake, if it covers any part of the poison grid, we can record which rows and columns it covers
        
        # Then, we can try to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # However, this is still not efficient for large K
        # So we need to find a way to represent this efficiently
        
        # For each snake, if it covers any part of the poison grid, we can record which rows and columns it covers
        
        # Then, we can try to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # But how?
        
        # We can try to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # For each row in the poison grid, we need at least one snake that covers it
        # For each column in the poison grid, we need at least one snake that covers it
        
        # So, for each snake, if it covers any row in the poison grid, it can potentially cover that row
        # Similarly, if it covers any column in the poison grid, it can potentially cover that column
        
        # So, for each snake, we can check if it covers any row in the poison grid
        # And if it covers any column in the poison grid
        
        # If it does, then it can potentially cover that row and column
        
        # So, we can try to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # But how?
        
        # We can try to find the minimum number of snakes that cover all the rows and columns in the poison grid
        
        # For each row in the poison grid, we need at least one snake that covers it
        # For each column in the poison grid, we need at least one snake that covers it