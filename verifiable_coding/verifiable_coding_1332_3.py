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
        
        # Find the lowest common ancestor (LCA) of i and j
        # Move both nodes up until they meet
        a, b = i, j
        while a != b:
            if a > b:
                a = a // 2
            else:
                b = b // 2
        
        # The distance is the sum of the steps taken to reach the LCA
        dist = 0
        a, b = i, j
        while a != b:
            if a > b:
                a = a // 2
                dist += 1
            else:
                b = b // 2
                dist += 1
        
        results.append(str(dist))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()