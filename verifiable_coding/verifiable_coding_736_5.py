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
        
        # Find the character that minimizes the absolute value of the total points
        # The optimal choice is to change all characters to the same character
        # which is the one that minimizes the absolute value of the total points
        # We try all 26 letters and choose the one with minimum absolute value
        
        min_abs = float('inf')
        best_char = 'a'
        
        for c in range(ord('a'), ord('z') + 1):
            total = 0
            for ch in S:
                diff = ord(ch) - c
                if diff > 0:
                    total += diff
                elif diff < 0:
                    total -= abs(diff)
            abs_total = abs(total)
            if abs_total < min_abs:
                min_abs = abs_total
                best_char = chr(c)
        
        results.append(str(min_abs))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()