import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    Q = int(data[0])
    index = 1
    
    for _ in range(Q):
        n = int(data[index])
        u = int(data[index+1])
        v = int(data[index+2])
        index += 3
        
        # Compute the path from u to v
        path = []
        while u != v:
            if u < v:
                path.append('left')
                u = u * 2
            else:
                path.append('right')
                u = u // 2
        
        # Count the number of pairs (w, t) with the same path
        # The path is uniquely determined by the sequence of moves
        # So we need to find all (w, t) such that the path from w to t is the same as the path from u to v
        
        # The path length is len(path)
        # The number of such pairs is (n - len(path) + 1) ** 2
        # Because for each step in the path, we can choose any node in the range [1, n - len(path) + 1]
        # So the answer is (n - len(path) + 1) ** 2
        
        length = len(path)
        ans = (n - length + 1) ** 2
        print(ans)

if __name__ == '__main__':
    solve()