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
        count = [0] * 9  # indexes 0-8, but 1-8 are used
        for num in a:
            count[num] += 1
        
        # Calculate maximum beauty
        beauty = 0
        current = 1
        for i in range(1, 9):
            if count[i] > 0:
                beauty += 1
                current = i
            elif count[i] == 0 and current < i:
                # We can't form a sequence up to i, so break
                break
        results.append(str(beauty))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()