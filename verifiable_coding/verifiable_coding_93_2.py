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
        
        # Create a map from present to its position in the stack
        pos = {present: i for i, present in enumerate(a)}
        
        # Preprocess the list of presents to send
        b_positions = [pos[present] for present in b]
        
        # Initialize the current position in the stack
        current_pos = -1
        
        total_time = 0
        
        for i in range(m):
            # Find the position of the current present in the stack
            target_pos = b_positions[i]
            
            # Calculate the time to retrieve the present
            k = current_pos - target_pos
            time = 2 * k + 1
            total_time += time
            
            # Update the current position to the target position
            current_pos = target_pos
        
        results.append(total_time)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()