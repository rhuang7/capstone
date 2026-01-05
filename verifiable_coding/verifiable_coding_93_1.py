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
        
        # For each present in b, find the next present in b that comes after it
        next_in_b = [m] * m
        for i in range(m-1, -1, -1):
            next_in_b[i] = i + 1 if i + 1 < m else m
        
        # Calculate the minimum time
        time = 0
        current_pos = -1
        for i in range(m):
            current_b_pos = b_positions[i]
            if current_b_pos < current_pos:
                # The present is below the previous one, so we need to reorder
                # The number of presents above is (current_pos - current_b_pos)
                time += 2 * (current_pos - current_b_pos) + 1
                # After reordering, the current present is at the top
                current_pos = current_b_pos
            else:
                # The present is above the previous one, so we just take it
                time += 2 * (current_pos - current_b_pos) + 1
                current_pos = current_b_pos
        
        results.append(time)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()