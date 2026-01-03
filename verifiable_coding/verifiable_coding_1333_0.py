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
        
        # Check if B is valid
        valid = True
        for i in range(N):
            if i > 0 and B[i] < B[i-1]:
                valid = False
                break
            if i > 0 and (B[i] & B[i-1]) != B[i-1]:
                valid = False
                break
        if not valid:
            results.append(0)
            continue
        
        # Calculate the number of valid sequences A
        res = 1
        prev = 0
        for i in range(N):
            if i == 0:
                prev = B[0]
            else:
                if (B[i] & prev) != prev:
                    res = 0
                    break
                prev = B[i]
            # The number of ways to choose A[i] is the number of bits that can be set in B[i] but not in B[i-1]
            # So we calculate the number of bits that can be set in B[i] but not in B[i-1]
            diff = B[i] ^ B[i-1]
            cnt = bin(diff).count('1')
            res = (res * cnt) % MOD
        results.append(res)
    
    for result in results:
        print(result)

if __name__ == '__main__':
    solve()