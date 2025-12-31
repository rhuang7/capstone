import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    idx = 1
    for _ in range(T):
        P = data[idx]
        idx += 1
        
        max_jump = 1
        days = 0
        
        i = 0
        while i < len(P):
            if P[i] == '#':
                i += 1
                continue
            # Find the next '#'
            j = i + 1
            while j < len(P) and P[j] == '.':
                j += 1
            if j >= len(P):
                break
            required = j - i
            if required > max_jump:
                days += 1
                max_jump = required
            i = j + 1
        
        results.append(str(days))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()