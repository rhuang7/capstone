import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Count occurrences of each octave tone
        count = [0] * 9  # 1-based indexing
        for num in a:
            count[num] += 1
        
        # Calculate maximum beauty
        beauty = 0
        current = 1
        while current <= 8:
            if count[current] > 0:
                beauty += 1
                current += 1
            else:
                # Try to find a higher octave tone to swap with
                for i in range(current + 1, 9):
                    if count[i] > 0:
                        # Swap current and i
                        count[current] += 1
                        count[i] -= 1
                        beauty += 1
                        current = i + 1
                        break
                else:
                    # No higher octave tone available
                    break
        
        results.append(str(beauty))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()