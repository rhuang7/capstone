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
        shares = []
        for _ in range(N):
            a = int(data[idx])
            b = int(data[idx + 1])
            shares.append((a, b))
            idx += 2
        
        # Sort shares by a_i in ascending order and then by b_i in descending order
        shares.sort(key=lambda x: (x[0], -x[1]))
        
        # Greedy selection: select shares with increasing b_i
        count = 0
        prev_b = -1
        for a, b in shares:
            if b > prev_b:
                count += 1
                prev_b = b
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()