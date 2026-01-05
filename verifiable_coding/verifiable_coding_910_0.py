import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        s = data[index]
        index += 1
        N = int(data[index])
        index += 1
        
        # Calculate total number of keys
        total_keys = 12 * N
        
        # Calculate the total steps in the pattern
        total_steps = sum(2 if c == 'T' else 1 for c in s)
        
        # If the pattern steps exceed the total keys, no valid plays
        if total_steps > total_keys:
            results.append(0)
            continue
        
        # Find the number of valid starting positions
        valid_start_positions = 0
        
        # For each possible starting position
        for start in range(total_keys):
            # Check if the pattern can be played starting at 'start'
            current = start
            valid = True
            for c in s:
                if c == 'T':
                    current += 2
                else:
                    current += 1
                if current > total_keys:
                    valid = False
                    break
            if valid:
                valid_start_positions += 1
        
        # For each valid starting position, count the number of times the pattern can be repeated
        # The pattern can be repeated k times such that the total steps is <= total_keys
        max_repeats = total_keys // total_steps
        
        # Total plays = valid_start_positions * max_repeats
        results.append(valid_start_positions * max_repeats)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()