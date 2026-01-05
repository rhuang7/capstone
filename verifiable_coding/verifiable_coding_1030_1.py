import sys

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
                path.append('L')
                u = u * 2
            else:
                path.append('R')
                u = u // 2
        
        # Count the number of pairs (w, t) that have the same path
        # The path is uniquely determined by the sequence of moves
        # So we need to find all pairs (w, t) such that the path from w to t is the same as the path from u to v
        
        # The path is a sequence of moves, and the number of such pairs is 2^k, where k is the length of the path
        # But we have to ensure that w and t are within 1 to n
        
        # The number of valid pairs is (number of possible starting points) * (number of possible ending points)
        # The path length is len(path)
        # The number of possible starting points is (n - 2^len(path) + 1)
        # The number of possible ending points is (n - 2^len(path) + 1)
        # So the total number of pairs is (n - 2^len(path) + 1) ** 2
        
        k = len(path)
        if k == 0:
            # u == v, so all pairs (w, w) are valid
            ans = n
        else:
            power = 1 << k
            if power > n:
                ans = 0
            else:
                ans = (n - power + 1) ** 2
        
        print(ans)

if __name__ == '__main__':
    solve()