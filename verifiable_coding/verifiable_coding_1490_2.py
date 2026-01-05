import sys

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
        idx += 1
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Count frequency of each height
        freq = {}
        for h in a:
            freq[h] = freq.get(h, 0) + 1
        
        # Calculate minimum kills
        kills = 0
        for h in freq:
            count = freq[h]
            # If count is 1, it's a single kill
            # If count is even, it's count//2 kills (pair kills)
            # If count is odd, it's (count//2) + 1 kills (one single, rest pairs)
            kills += count // 2
            if count % 2 == 1:
                kills += 1
        
        results.append(str(kills))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()