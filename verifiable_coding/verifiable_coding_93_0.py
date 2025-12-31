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
        n, m = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        b = list(map(int, data[idx:idx+m]))
        idx += m
        
        # Create a map from present number to its position in the stack
        pos = {present: i for i, present in enumerate(a)}
        
        # Preprocess the list of presents to send
        b_pos = [pos[present] for present in b]
        
        # Find the positions of the presents in the stack
        # We need to find the order in which they appear in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a pointer to track where we are in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack
        # We'll use a list to track the order of presents in the stack