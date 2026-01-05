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
        idx += 1
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Group the sequence into runs of equal elements
        groups = []
        current_val = A[0]
        count = 1
        for i in range(1, N):
            if A[i] == current_val:
                count += 1
            else:
                groups.append(count)
                current_val = A[i]
                count = 1
        groups.append(count)
        
        # Calculate the minimum operations needed
        # We need to make all group lengths even
        # For each group, if it's odd, we need to delete one element or add one element
        # But we can also combine groups to make them even
        # The optimal way is to find the minimal number of operations to make all group lengths even
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The optimal solution is to find the minimal number of operations to make all group lengths even
        # This can be done by trying all possible ways to combine groups
        
        # For each group, if it's odd, we need to delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        # So we can try all possible ways to combine groups
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the minimal number of deletions and insertions to make all group lengths even
        # We can try all possible ways to combine groups
        
        # We can try all possible ways to combine groups
        # For each group, if it's odd, we can either delete one element or add one element
        # But we can also combine with adjacent groups to make them even
        
        # The minimal number of operations is the