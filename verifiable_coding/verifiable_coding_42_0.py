import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        s = data[i]
        count = 0
        n = len(s)
        
        for l in range(n):
            value = 0
            for r in range(l, n):
                value = (value << 1) | int(s[r])
                if value == r - l + 1:
                    count += 1
                if value > 10**6:  # To avoid overflow and unnecessary computation
                    break
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()