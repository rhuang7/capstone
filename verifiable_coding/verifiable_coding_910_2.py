import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    idx = 1
    
    results = []
    
    for _ in range(T):
        s = data[idx]
        idx += 1
        N = int(data[idx])
        idx += 1
        
        # Calculate total number of keys
        total_keys = 12 * N
        
        # Calculate the total length of the pattern
        pattern_length = len(s)
        
        # Calculate the total number of steps in the pattern
        total_steps = 0
        for c in s:
            if c == 'T':
                total_steps += 2
            else:
                total_steps += 1
        
        # Calculate the number of valid starting positions
        # A starting position is valid if the pattern can be played without going out of bounds
        valid_start_positions = 0
        
        for start in range(total_keys):
            # Check if the pattern can be played starting at 'start'
            # We need to find the maximum number of times the pattern can be repeated
            # without exceeding total_keys
            current = start
            repeats = 0
            while True:
                # Check if we can play the pattern once
                can_play = True
                for c in s:
                    if c == 'T':
                        current += 2
                    else:
                        current += 1
                    if current > total_keys:
                        can_play = False
                        break
                if not can_play:
                    break
                repeats += 1
            valid_start_positions += 1
        
        results.append(valid_start_positions)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()