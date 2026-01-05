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
        voters.sort(key=lambda x: -x[0])
        
        # Use a set to track the current voters
        current = set()
        total_cost = 0
        
        for m, p in voters:
            # If the voter is not already in the set, we need to buy them
            if m not in current:
                total_cost += p
                current.add(m)
                # Add all the m_i voters to the set
                for _ in range(m):
                    if _ not in current:
                        current.add(_)
        
        results.append(total_cost)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()