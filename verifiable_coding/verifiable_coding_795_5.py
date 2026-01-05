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
        
        # Minimum number of players required
        min_players = 1
        if N > 2 * L:
            min_players = (N + 1) // 2
        if K < min_players:
            results.append("-1")
            continue
        
        # Assign bowlers
        res = []
        for i in range(N):
            if i % 2 == 0:
                res.append(1)
            else:
                res.append(2)
        
        # Check if any player exceeds L overs
        count = [0] * (K + 1)
        for b in res:
            count[b] += 1
        for i in range(1, K + 1):
            if count[i] > L:
                results.append("-1")
                break
        else:
            results.append(" ".join(map(str, res)))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()