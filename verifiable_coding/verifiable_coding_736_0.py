import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        S = data[i].strip()
        if not S:
            results.append(0)
            continue
        
        # Calculate the total points for converting all characters to 'a'
        total = 0
        for c in S:
            total += ord(c) - ord('a')
        
        # The minimum absolute value is the minimum between total and (25 - total)
        min_abs = min(total, 25 - total)
        results.append(str(min_abs))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()