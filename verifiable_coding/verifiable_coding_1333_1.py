import sys
MOD = 10**9 + 7

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
        B = list(map(int, data[idx:idx+N]))
        idx += N
        
        if B[0] == 0:
            results.append(1)
            continue
        
        # Check if B is valid
        valid = True
        for i in range(N):
            if i == 0:
                if B[i] != 0:
                    valid = False
                    break
            else:
                if B[i] < B[i-1]:
                    valid = False
                    break
        if not valid:
            results.append(0)
            continue
        
        # Compute the number of valid sequences A
        res = 1
        prev = 0
        for i in range(N):
            if i == 0:
                prev = B[i]
            else:
                if B[i] == B[i-1]:
                    res = (res * 2) % MOD
                else:
                    res = (res * 1) % MOD
                    prev = B[i]
        results.append(res)
    
    for r in results:
        print(r)

if __name__ == '__main__':
    solve()