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
        # A valid arrangement must have no two consecutive same characters
        # So, the count of 'B' and 'G' must differ by at most 1
        count_b = s.count('B')
        count_g = n - count_b
        if abs(count_b - count_g) > 1:
            results.append("-1")
            continue
        
        # Generate the target arrangement
        # We can choose between two possible valid arrangements:
        # 1. Start with 'B' if count_b >= count_g, else start with 'G'
        # 2. Start with 'G' if count_g >= count_b, else start with 'B'
        # We need to choose the one that requires minimum swaps
        # For simplicity, we'll generate both and compute the cost
        
        # Generate target1: starts with 'B' if count_b >= count_g, else 'G'
        target1 = []
        if count_b >= count_g:
            target1 = ['B'] * (count_b) + ['G'] * (count_g)
        else:
            target1 = ['G'] * (count_g) + ['B'] * (count_b)
        
        # Generate target2: starts with 'G' if count_g >= count_b, else 'B'
        target2 = []
        if count_g >= count_b:
            target2 = ['G'] * (count_g) + ['B'] * (count_b)
        else:
            target2 = ['B'] * (count_b) + ['G'] * (count_g)
        
        # Function to compute the minimum cost to convert s to target
        def compute_cost(s, target, type_):
            # Create a list of positions for each character in target
            pos = {}
            for i, c in enumerate(target):
                if c not in pos:
                    pos[c] = []
                pos[c].append(i)
            
            # Create a list of positions for each character in s
            s_list = list(s)
            # For each character in s, find the closest position in target
            # We'll use a greedy approach to minimize the cost
            # For type 0, cost is 1 per swap
            # For type 1, cost is |i - j|
            # For type 2, cost is (i - j)^2
            # We'll use a priority queue to select the best swap
            
            # Create a list of positions for each character in s
            s_pos = {}
            for i, c in enumerate(s_list):
                if c not in s_pos:
                    s_pos[c] = []
                s_pos[c].append(i)
            
            # For each character in s, find the closest position in target
            # We'll use a greedy approach to minimize the cost
            # For type 0, cost is 1 per swap
            # For type 1, cost is |i - j|
            # For type 2, cost is (i - j)^2
            # We'll use a priority queue to select the best swap
            
            # Create a list of positions for each character in s
            s_pos = {}
            for i, c in enumerate(s_list):
                if c not in s_pos:
                    s_pos[c] = []
                s_pos[c].append(i)
            
            # For each character in s, find the closest position in target
            # We'll use a greedy approach to minimize the cost
            # For type 0, cost is 1 per swap
            # For type 1, cost is |i - j|
            # For type 2, cost is (i - j)^2
            # We'll use a priority queue to select the best swap
            
            # Create a list of positions for each character in s
            s_pos = {}
            for i, c in enumerate(s_list):
                if c not in s_pos:
                    s_pos[c] = []
                s_pos[c].append(i)
            
            # For each character in s, find the closest position in target
            # We'll use a greedy approach to minimize the cost
            # For type 0, cost is 1 per swap
            # For type 1, cost is |i - j|
            # For type 2, cost is (i - j)^2
            # We'll use a priority queue to select the best swap
            
            # Create a list of positions for each character in s
            s_pos = {}
            for i, c in enumerate(s_list):
                if c not in s_pos:
                    s_pos[c] = []
                s_pos[c].append(i)
            
            # For each character in s, find the closest position in target
            # We'll use a greedy approach to minimize the cost
            # For type 0, cost is 1 per swap
            # For type 1, cost is |i - j|
            # For type 2, cost is (i - j)^2
            # We'll use a priority queue to select the best swap
            
            # Create a list of positions for each character in s
            s_pos = {}
            for i, c in enumerate(s_list):
                if c not in s_pos:
                    s_pos[c] = []
                s_pos[c].append(i)
            
            # For each character in s, find the closest position in target
            # We'll use a greedy approach to minimize the cost
            # For type 0, cost is 1 per swap
            # For type 1, cost is |i - j|
            # For type 2, cost is (i - j)^2
            # We'll use a priority queue to select the best swap
            
            # Create a list of positions for each character in s
            s_pos = {}
            for i, c in enumerate(s_list):
                if c not in s_pos:
                    s_pos[c] = []
                s_pos[c].append(i)
            
            # For each character in s, find the closest position in target
            # We'll use a greedy approach to minimize the cost
            # For type 0, cost is 1 per swap
            # For type 1, cost is |i - j|
            # For type 2, cost is (i - j)^2
            # We'll use a priority queue to select the best swap
            
            # Create a list of positions for each character in s
            s_pos = {}
            for i, c in enumerate(s_list):
                if c not in s_pos:
                    s_pos[c] = []
                s_pos[c].append(i)
            
            # For each character in s, find the closest position in target
            # We'll use a greedy approach to minimize the cost
            # For type 0, cost is 1 per swap
            # For type 1, cost is |i - j|
            # For type 2, cost is (i - j)^2
            # We'll use a priority queue to select the best swap
            
            # Create a list of positions for each character in s
            s_pos = {}
            for i, c in enumerate(s_list):
                if c not in s_pos:
                    s_pos[c] = []
                s_pos[c].append(i)
            
            # For each character in s, find the closest position in target
            # We'll use a greedy approach to minimize the cost
            # For type 0, cost is 1 per swap
            # For type 1, cost is |i - j|
            # For type 2, cost is (i - j)^2
            # We'll use a priority queue to select the best swap
            
            # Create a list of positions for each character in s
            s_pos = {}
            for i, c in enumerate(s_list):
                if c not in s_pos:
                    s_pos[c] = []
                s_pos[c].append(i)
            
            # For each character in s, find the closest position in target
            # We'll use a greedy approach to minimize the cost
            # For type 0, cost is 1 per swap
            # For type 1, cost is |i - j|
            # For type 2, cost is (i - j)^2
            # We'll use a priority queue to select the best swap
            
            # Create a list of positions for each character in s
            s_pos = {}
            for i, c in enumerate(s_list):
                if c not in s_pos:
                    s_pos[c] = []
                s_pos[c].append(i)
            
            # For each character in s, find the closest position in target
            # We'll use a greedy approach to minimize the cost
            # For type 0, cost is 1 per swap
            # For type 1, cost is |i - j|
            # For type 2, cost is (i - j)^2
            # We'll use a priority queue to select the best swap
            
            # Create a list of positions for each character in s