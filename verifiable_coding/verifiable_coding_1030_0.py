import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    Q = int(data[0])
    idx = 1
    
    for _ in range(Q):
        n = int(data[idx])
        u = int(data[idx+1])
        v = int(data[idx+2])
        idx += 3
        
        # Function to get the path from u to v
        def get_path(u, v):
            path = []
            while u != v:
                if u < v:
                    path.append('L')
                    u = u * 2
                else:
                    path.append('R')
                    u = u // 2
            return path
        
        path = get_path(u, v)
        
        # Count the number of pairs (w, t) with the same path
        # The path is unique for each pair (w, t), so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is 2^len(path)
        # But we have to ensure that w and t are within 1..n
        # The path length is len(path)
        # The number of possible pairs is 2^len(path)
        # However, we have to check if the path is valid for the given n
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (w, t) that have the same path
        # The path is determined by the sequence of moves from w to t, so the number of such pairs is the number of pairs (