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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        max_len = 0
        freq = {}
        for num in a:
            freq[num] = freq.get(num, 0) + 1
        
        for a_val in freq:
            for b_val in freq:
                if a_val == b_val:
                    max_len = max(max_len, freq[a_val])
                else:
                    left = freq[a_val]
                    right = freq[b_val]
                    max_len = max(max_len, left + right + min(left, right))
        
        results.append(str(max_len))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()