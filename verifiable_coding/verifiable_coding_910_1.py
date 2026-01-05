import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    for _ in range(T):
        s = data[index]
        index += 1
        N = int(data[index])
        index += 1
        
        # Compute total number of keys
        total_keys = 12 * N
        
        # Compute the total steps in the pattern
        total_steps = sum(2 if c == 'T' else 1 for c in s)
        
        # If the pattern is too long to fit even once, no valid plays
        if total_steps > total_keys:
            print(0)
            continue
        
        # Compute the number of valid starting positions
        # A valid starting position is one where the pattern can be played at least once
        # without going out of bounds
        valid_starts = 0
        
        for start in range(total_keys):
            pos = start
            valid = True
            for c in s:
                if c == 'T':
                    pos += 2
                else:
                    pos += 1
                if pos > total_keys:
                    valid = False
                    break
            if valid:
                valid_starts += 1
        
        # Each valid start can be repeated any number of times (including 0)
        # So total plays is valid_starts * (number of possible repetitions)
        # The number of repetitions is determined by how many times the pattern can be repeated
        # without exceeding total_keys
        
        # Compute how many times the pattern can be repeated
        # The pattern length in steps is total_steps
        # So the number of repetitions is floor((total_keys - start) / total_steps)
        # But since we're counting all possible repetitions, it's simply the number of valid starts
        
        # The number of possible repetitions for each valid start is floor((total_keys - start) / total_steps) + 1
        # But since we're counting all possible repetitions, it's simply the number of valid starts multiplied by the number of possible repetitions
        
        # However, since the problem says that two plays differ if the pattern is repeated a different number of times,
        # we need to count all possible repetitions for each valid start
        
        # So the total number of plays is valid_starts * (number of possible repetitions for each start)
        
        # But how to compute that?
        # For each valid start, the number of repetitions is floor((total_keys - start) / total_steps) + 1
        # But we can't compute that for each start due to time constraints
        
        # Instead, we can compute the number of possible repetitions for the pattern
        # The pattern can be repeated k times if k * total_steps <= total_keys
        # So k_max = floor(total_keys / total_steps)
        # So the number of possible repetitions is k_max + 1 (including 0)
        
        # But since the pattern can be repeated any number of times (including 0), the number of possible repetitions is k_max + 1
        
        # However, we need to ensure that the pattern can be played at least once
        # So k_max must be >= 1
        
        # So the total number of plays is valid_starts * (k_max + 1)
        
        # But we need to compute k_max
        if total_steps == 0:
            k_max = 0
        else:
            k_max = total_keys // total_steps
        
        if k_max == 0:
            print(0)
        else:
            print(valid_starts * (k_max + 1))
            
if __name__ == '__main__':
    solve()