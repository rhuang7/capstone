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
        
        # Calculate the total number of steps in the pattern
        total_steps = sum(2 if c == 'T' else 1 for c in s)
        
        # Check if the pattern can be played starting from any key
        # The pattern must fit within the total_keys
        if total_steps > total_keys:
            results.append(0)
            continue
        
        # Calculate the number of valid starting positions
        # The pattern can be played starting from any key such that the pattern fits
        # Also, the pattern can be repeated any number of times as long as it doesn't exceed the total_keys
        # So the number of valid starting positions is total_keys - total_steps + 1
        
        valid_start_positions = total_keys - total_steps + 1
        
        # The number of different plays is the number of valid starting positions multiplied by the number of possible repetitions
        # The number of possible repetitions is the number of times the pattern can be repeated without exceeding total_keys
        
        # The number of repetitions is the maximum number of times the pattern can be repeated
        # This is equal to the number of times the pattern can be repeated such that the total steps do not exceed total_keys
        # So the number of repetitions is (total_keys // total_steps)
        
        max_repetitions = total_keys // total_steps
        
        # The number of different plays is valid_start_positions * max_repetitions
        results.append(valid_start_positions * max_repetitions)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()