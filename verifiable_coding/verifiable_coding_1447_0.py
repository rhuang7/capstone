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
        valid = True
        for i in range(N):
            num = A[i]
            if num in pos:
                if pos[num] >= i:
                    valid = False
                    break
            pos[num] = i
        
        if valid:
            results.append("YES")
        else:
            results.append("NO")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()