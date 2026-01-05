import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    idx = 1
    results = []
    
    for _ in range(N):
        i = int(data[idx])
        j = int(data[idx+1])
        idx += 2
        
        # Find the length of the shortest path between i and j
        # The path is the number of steps to move up to the lowest common ancestor (LCA)
        # and then down to the other node
        # So we find the LCA by moving the deeper node up until both are at the same depth
        # Then move both up until they meet
        
        # Find the depth of each node
        def depth(node):
            d = 0
            while node > 1:
                node >>= 1
                d += 1
            return d
        
        d_i = depth(i)
        d_j = depth(j)
        
        # Bring the deeper node up to the same depth
        while d_i > d_j:
            i >>= 1
            d_i -= 1
        while d_j > d_i:
            j >>= 1
            d_j -= 1
        
        # Now find the LCA by moving both up until they meet
        steps = 0
        while i != j:
            i >>= 1
            j >>= 1
            steps += 2
        
        results.append(str(steps))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()