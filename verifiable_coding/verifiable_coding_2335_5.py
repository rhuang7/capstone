import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        # For each position, find the earliest position >= current value that is not yet occupied
        # We'll track which positions are occupied
        occupied = [False] * (n + 1)  # 1-based indexing
        # For each value from 1 to n, find its position in the permutation
        pos = [0] * (n + 1)  # pos[i] is the position of value i in the permutation
        for i in range(n):
            pos[p[i]] = i + 1  # 1-based position
        
        # Check if the permutation is valid
        valid = True
        for i in range(1, n + 1):
            # Find the earliest position >= i that is not occupied
            r = None
            for j in range(i, n + 1):
                if not occupied[j]:
                    r = j
                    break
            if r is None:
                valid = False
                break
            # Check if the position r is the one chosen for i
            if pos[i] != r:
                valid = False
                break
            occupied[r] = True
        
        results.append("Yes" if valid else "No")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()