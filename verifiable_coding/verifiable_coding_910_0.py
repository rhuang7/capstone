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
        
        # Calculate the total number of steps in the pattern
        total_steps = sum(2 if c == 'T' else 1 for c in s)
        
        # If the pattern is too long to fit even once, no valid plays
        if total_steps > total_keys:
            results.append(0)
            continue
        
        # Find all possible starting positions
        valid_starts = 0
        
        # For each possible starting position
        for start in range(total_keys):
            # Check if the pattern can be played starting at 'start'
            valid = True
            current = start
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
        
        # For each valid starting position, count how many times the pattern can be repeated
        # The pattern can be repeated k times if the total steps * k <= total_keys - start
        # So k can be from 1 to max_repeats
        # For each valid start, the number of possible repetitions is max_repeats
        # So total plays = valid_starts * max_repeats
        
        # Calculate max_repeats for each valid start
        max_repeats = 0
        for start in range(total_keys):
            valid = True
            current = start
            for c in s:
                if c == 'T':
                    current += 2
                else:
                    current += 1
                if current > total_keys:
                    valid = False
                    break
            if valid:
                # Calculate how many times the pattern can be repeated
                # total_steps * k <= total_keys - start
                # k <= (total_keys - start) // total_steps
                max_repeats = (total_keys - start) // total_steps
                valid_starts *= (max_repeats + 1)
        
        results.append(valid_starts)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()