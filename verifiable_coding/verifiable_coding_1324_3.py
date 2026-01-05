import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        # The minimum sum of K distinct positive integers is 1 + 2 + ... + K = K*(K+1)//2
        min_sum = K * (K + 1) // 2
        if N < min_sum:
            results.append(-1)
            continue
        
        # The maximum possible gcd is the maximum d such that d * K <= N and d * (K*(K+1)//2) <= N
        # We can use binary search to find this d
        low = 1
        high = N // K
        best = -1
        
        while low <= high:
            mid = (low + high) // 2
            total = mid * K * (K + 1) // 2
            if total <= N:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        
        results.append(best)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()