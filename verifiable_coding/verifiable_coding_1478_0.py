import sys
import math

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
        
        # Find all positions where the value is -1
        unknowns = [i for i in range(N) if A[i] == -1]
        if not unknowns:
            # All elements are known, check if it's periodic
            period = None
            for i in range(1, N):
                if A[i] != A[i - 1]:
                    period = i
                    break
            if period is None:
                # All elements are the same, period can be arbitrarily large
                results.append("inf")
            else:
                # Check if the sequence is periodic with period 'period'
                valid = True
                for i in range(period, N):
                    if A[i] != A[i - period]:
                        valid = False
                        break
                if valid:
                    results.append(str(period))
                else:
                    results.append("impossible")
            continue
        
        # At least one unknown, try to find possible periods
        max_possible = N - 1
        possible_periods = set()
        
        # Try all possible periods from 1 to N-1
        for K in range(1, N):
            # Check if the sequence can be filled with -1s to make it periodic with period K
            valid = True
            for i in range(N):
                pos = i % K
                if A[i] != -1:
                    if A[i] != (pos + 1):
                        valid = False
                        break
            if valid:
                possible_periods.add(K)
        
        if len(possible_periods) == 0:
            results.append("impossible")
        else:
            # The maximum possible period is the maximum in possible_periods
            results.append(str(max(possible_periods)))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()