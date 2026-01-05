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
        total = 0
        
        for m, p in voters:
            if m == 0:
                # This voter can't be convinced by others, must be bought
                total += p
                current.add(m)
            else:
                # Check if this voter is already in the set
                if m not in current:
                    # This voter can be convinced by others, but we need to make sure
                    # that the required voters are already in the set
                    # So we need to buy this voter
                    total += p
                    current.add(m)
                    # Add all the m_i voters to the set
                    for i in range(m):
                        if i + 1 not in current:
                            current.add(i + 1)
        
        results.append(total)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()