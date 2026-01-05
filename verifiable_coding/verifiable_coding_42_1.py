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
            val = 0
            for r in range(l, n):
                val = (val << 1) | int(s[r])
                if val == r - l + 1:
                    count += 1
                if val > 10**6:  # Since 2^20 is over 1e6, and max substring length is 2e5, this is safe
                    break
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()