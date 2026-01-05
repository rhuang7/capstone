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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        from collections import defaultdict
        count = defaultdict(int)
        for num in A:
            count[num] += 1
        
        freq = list(count.values())
        if len(freq) != len(set(freq)):
            results.append("NO")
            continue
        
        pos = {}
        for i in range(N):
            num = A[i]
            if num in pos:
                results.append("NO")
                break
            pos[num] = i
        
        else:
            results.append("YES")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()