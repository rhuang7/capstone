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
        
        # Sort voters by m_i in descending order
        voters.sort(reverse=True, key=lambda x: x[0])
        
        # Use a set to track the current voters
        current = set()
        total_cost = 0
        
        for m, p in voters:
            if m == 0:
                # This voter can't be convinced through the second way
                total_cost += p
                current.add(m)
            else:
                # Check if this voter is already in the set
                if m not in current:
                    # Add this voter and all m_i voters
                    current.add(m)
                    # Add all m_i voters (but we don't have their info, so we assume they are already in the set)
                    # So we just add this voter and pay the cost
                    total_cost += p
        
        results.append(total_cost)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()