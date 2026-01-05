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
        K = int(data[idx+1])
        L = int(data[idx+2])
        idx += 3
        
        # Check if it's possible to assign bowlers
        if K < 1 or L < 1:
            results.append("-1")
            continue
        
        # Minimum number of players needed is 2 (since no two consecutive overs can have same bowler)
        if K < 2:
            results.append("-1")
            continue
        
        # Check if total possible overs is enough
        max_overs = K * L
        if N > max_overs:
            results.append("-1")
            continue
        
        # Check if consecutive overs can be handled
        if N > K * 2:
            results.append("-1")
            continue
        
        # Assign bowlers in a repeating pattern
        result = []
        for i in range(N):
            # Alternate between players 1 and 2
            if i % 2 == 0:
                result.append(1)
            else:
                result.append(2)
        
        # Check if any player exceeds L overs
        count = [0] * (K + 1)
        for b in result:
            count[b] += 1
        for i in range(1, K + 1):
            if count[i] > L:
                results.append("-1")
                break
        else:
            results.append(" ".join(map(str, result)))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()