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
        
        if S == R:
            results.append("YES")
            continue
        
        count_S = [0, 0]
        count_R = [0, 0]
        
        for c in S:
            count_S[int(c)] += 1
        for c in R:
            count_R[int(c)] += 1
        
        if count_S == count_R:
            results.append("YES")
        else:
            results.append("NO")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()