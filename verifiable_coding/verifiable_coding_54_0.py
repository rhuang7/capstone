import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    q = int(data[idx])
    idx += 1
    
    results = []
    
    for _ in range(q):
        n = int(data[idx])
        idx += 1
        s = list(map(int, data[idx:idx+n]))
        idx += n
        
        count = {}
        for num in s:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Convert to exponents of 2
        exp = {}
        for num in count:
            exp[num] = count[num]
        
        # Start from 1 (2^0) and go up to 2048 (2^11)
        for i in range(1, 12):
            if 2 ** i in exp:
                exp[2 ** i] = exp[2 ** i]
            else:
                exp[2 ** i] = 0
        
        # Try to build up to 2048
        for i in range(11, 0, -1):
            if exp[2 ** i] > 0:
                # Try to combine with lower exponents
                while exp[2 ** i] > 0:
                    exp[2 ** (i - 1)] += exp[2 ** i]
                    exp[2 ** i] = 0
                # Check if we have enough to make 2048
                if exp[2 ** 11] >= 1:
                    results.append("YES")
                    break
        else:
            results.append("NO")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()