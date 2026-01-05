import sys

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        S = data[idx]
        idx += 1
        R = data[idx]
        idx += 1
        
        if sorted(S) != sorted(R):
            results.append("NO")
        else:
            results.append("YES")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()