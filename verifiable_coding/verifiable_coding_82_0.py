import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        p = list(map(int, data[idx:idx + n]))
        idx += n
        
        # If n == 2, simply swap the two elements
        if n == 2:
            results.append(' '.join(map(str, [p[1], p[0]])))
            continue
        
        # For n >= 3, we can reverse the permutation
        reversed_p = p[::-1]
        if reversed_p != p:
            results.append(' '.join(map(str, reversed_p)))
        else:
            # If the permutation is already symmetric, we can swap the first two elements
            results.append(' '.join(map(str, [p[1], p[0]] + p[2:])))

    print('\n'.join(results))

if __name__ == '__main__':
    solve()