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
        K = int(data[idx+1])
        idx += 2
        S = data[idx]
        idx += 1
        
        # Precompute counts of 'a' and 'b' in S
        a_count = S.count('a')
        b_count = S.count('b')
        
        # Total number of 'a's in K repetitions
        total_a = a_count * K
        
        # Total number of 'b's in K repetitions
        total_b = b_count * K
        
        # Total number of 'ab' subsequences is total_a * total_b
        results.append(total_a * total_b)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()