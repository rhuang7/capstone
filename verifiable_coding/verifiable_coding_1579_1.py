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
        
        seen = set()
        unique = True
        
        for i in range(N):
            current_or = 0
            for j in range(i, N):
                current_or |= A[j]
                if current_or in seen:
                    unique = False
                    break
                seen.add(current_or)
            if not unique:
                break
        
        results.append("YES" if unique else "NO")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()