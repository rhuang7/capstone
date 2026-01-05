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
        
        has_even = False
        for num in A:
            if num % 2 == 0:
                has_even = True
                break
        
        if has_even:
            results.append("NO")
        else:
            results.append("YES")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()