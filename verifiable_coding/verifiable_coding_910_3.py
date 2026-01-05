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
        
        # Calculate the total number of keys
        total_keys = 12 * N
        
        # Calculate the length of the pattern
        pattern_len = len(s)
        
        # Calculate the total steps in the pattern
        total_steps = 0
        for c in s:
            if c == 'T':
                total_steps += 2
            else:
                total_steps += 1
        
        # Find the number of valid starting positions
        valid_starts = 0
        
        # Check for each possible starting position
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
                valid_starts += 1
        
        # Find the number of valid repetitions
        valid_repeats = 0
        
        # Check for each possible number of repetitions
        for repeat in range(1, total_keys + 1):
            current = 0
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
                valid_repeats += 1
        
        # Total number of different plays
        total = valid_starts * valid_repeats
        
        results.append(str(total))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()