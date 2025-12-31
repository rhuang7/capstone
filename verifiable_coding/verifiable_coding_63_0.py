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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        w = list(map(int, data[idx:idx+k]))
        idx += k
        
        a.sort()
        w.sort(reverse=True)
        
        total = 0
        # Assign maximums and minimums
        # For each friend, take the largest available and the smallest available
        # The rest can be anything, but we need to maximize the sum of max and min
        # So we take the largest k elements as maxes and the smallest k elements as mins
        # But since each friend gets w_i elements, we need to assign maxes and mins accordingly
        
        # Sort a
        a.sort()
        # Take the largest k elements as maxes
        maxes = a[-k:]
        # Take the smallest k elements as mins
        mins = a[:k]
        
        # The sum of maxes and mins is the total happiness
        total = sum(maxes) + sum(mins)
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()