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
            m_i = int(data[idx])
            p_i = int(data[idx + 1])
            voters.append((m_i, p_i))
            idx += 2
        
        # Sort voters by m_i in descending order
        voters.sort(reverse=True, key=lambda x: x[0])
        
        # Use a set to track the current voters
        current = set()
        total_cost = 0
        
        for m, p in voters:
            # If the voter is not already in the set, we need to buy them
            if m not in current:
                # Add the voter to the set
                current.add(m)
                # Add the cost
                total_cost += p
        
        results.append(str(total_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()