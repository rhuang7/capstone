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
                if val > 10**6:
                    break  # Since the maximum possible value for a substring is 2^20, which is about 1e6
        
        results.append(str(count))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()