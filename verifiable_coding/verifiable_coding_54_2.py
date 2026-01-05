import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    q = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(q):
        n = int(data[index])
        index += 1
        s = list(map(int, data[index:index + n]))
        index += n
        
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
        for i in range(11, -1, -1):
            if 2 ** i == 2048:
                if exp.get(2048, 0) >= 1:
                    results.append("YES")
                    break
            else:
                if exp.get(2 ** i, 0) >= 2:
                    exp[2 ** (i + 1)] = exp.get(2 ** (i + 1), 0) + exp[2 ** i] // 2
                    exp[2 ** i] = exp[2 ** i] % 2
        
        else:
            results.append("NO")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()