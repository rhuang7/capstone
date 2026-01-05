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
        type_ = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        n = len(s)
        
        # Check if it's possible to make the arrangement valid
        # A valid arrangement must alternate between B and G
        # So the count of B and G must differ by at most 1
        cnt_b = s.count('B')
        cnt_g = n - cnt_b
        if abs(cnt_b - cnt_g) > 1:
            results.append("-1")
            continue
        
        # Generate the target arrangement
        # We can choose to start with B or G, whichever is possible
        # We'll try both and choose the one with minimum cost
        # But for efficiency, we can just generate the target arrangement
        # based on the counts and the original string
        
        # Generate the target arrangement
        target = []
        if cnt_b > cnt_g:
            target = ['B'] * (cnt_b) + ['G'] * (cnt_g)
        else:
            target = ['G'] * (cnt_g) + ['B'] * (cnt_b)
        
        # Now we need to find the minimum cost to convert s to target
        # We can do this by matching the positions of B and G in s to the target
        # and calculating the cost accordingly
        
        # Create a list of positions for B and G in s
        b_pos = []
        g_pos = []
        for i, c in enumerate(s):
            if c == 'B':
                b_pos.append(i)
            else:
                g_pos.append(i)
        
        # Create a list of positions for B and G in target
        t_b_pos = []
        t_g_pos = []
        for i, c in enumerate(target):
            if c == 'B':
                t_b_pos.append(i)
            else:
                t_g_pos.append(i)
        
        # Now we need to match the B's in s to the B's in target
        # and G's in s to the G's in target
        # We can do this by matching the positions in order
        
        # For type 0, cost is 1 per swap
        # For type 1, cost is |i - j|
        # For type 2, cost is (i - j)^2
        
        # We'll calculate the cost for both possible target arrangements
        # and choose the one with minimum cost
        
        # Try to match B's in s to B's in target
        # and G's in s to G's in target
        # This is a greedy approach, matching the first B in s to the first B in target
        
        # We'll try both possible target arrangements (starting with B or G)
        # and choose the one with minimum cost
        
        # Function to calculate cost
        def calculate_cost(b1, g1, t_b, t_g, type_):
            cost = 0
            for i in range(len(b1)):
                cost += (t_b[i] - b1[i]) ** type_
            for i in range(len(g1)):
                cost += (t_g[i] - g1[i]) ** type_
            return cost
        
        # Try both possible target arrangements
        # First, target starts with B
        t_b = []
        t_g = []
        for i in range(n):
            if i % 2 == 0:
                t_b.append(i)
            else:
                t_g.append(i)
        
        # Second, target starts with G
        t_b2 = []
        t_g2 = []
        for i in range(n):
            if i % 2 == 0:
                t_g2.append(i)
            else:
                t_b2.append(i)
        
        # Now calculate cost for both target arrangements
        # But we need to match the B's and G's in s to the target
        # So we need to match the positions of B and G in s to the target
        
        # First, match B's in s to B's in target (starting with B)
        # and G's in s to G's in target (starting with B)
        # Then match B's in s to B's in target (starting with G)
        # and G's in s to G's in target (starting with G)
        
        # For the first case
        # B's in s are b_pos, B's in target are t_b
        # G's in s are g_pos, G's in target are t_g
        # We need to match them in order
        
        # For the second case
        # B's in s are b_pos, B's in target are t_b2
        # G's in s are g_pos, G's in target are t_g2
        
        # Now calculate the cost for both cases
        cost1 = calculate_cost(b_pos, g_pos, t_b, t_g, type_)
        cost2 = calculate_cost(b_pos, g_pos, t_b2, t_g2, type_)
        
        # Choose the minimum cost
        min_cost = min(cost1, cost2)
        results.append(str(min_cost))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()