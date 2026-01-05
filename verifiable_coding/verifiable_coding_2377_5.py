import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Find the sorted version of the array
        sorted_a = sorted(a)
        
        # Find the longest prefix of sorted_a that is a subsequence of a
        # This will give us the maximum number of elements that are already in the correct order
        # The rest need to be moved
        max_len = 0
        for i in range(n):
            if a[i] == sorted_a[i]:
                max_len += 1
            else:
                break
        
        # The minimum number of operations is n - max_len
        results.append(str(n - max_len))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()