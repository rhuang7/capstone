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
        voters = []
        for _ in range(n):
            m = int(data[idx])
            p = int(data[idx + 1])
            voters.append((m, p))
            idx += 2
        
        # Sort voters by m in descending order
        voters.sort(key=lambda x: -x[0])
        
        # Use a set to track the current voters
        current = set()
        total_cost = 0
        
        for m, p in voters:
            if m >= len(current):
                # Need to buy this voter
                total_cost += p
                current.add(m)
            else:
                # This voter can be added through the chain
                current.add(m)
        
        results.append(total_cost)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()