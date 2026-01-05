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
        b_indices = [pos[present] for present in b]
        
        # For each present in b, find the position in the stack and calculate time
        time = 0
        current_pos = -1
        for i in range(m):
            target_pos = b_indices[i]
            # The number of presents above is target_pos - current_pos - 1
            k = target_pos - current_pos - 1
            time += 2 * k + 1
            # After taking the present, the current_pos is updated to target_pos
            current_pos = target_pos
        
        results.append(str(time))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()