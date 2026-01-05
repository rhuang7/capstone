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
                current += 1
        
        results.append(beauty)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()