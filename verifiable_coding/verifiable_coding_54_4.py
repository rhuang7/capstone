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
        s = list(map(int, data[idx:idx + n]))
        idx += n
        
        # Count occurrences of each power of two
        count = {}
        for num in s:
            exp = num.bit_length() - 1
            count[exp] = count.get(exp, 0) + 1
        
        # Try to build up to 2048
        current = 11  # 2048 is 2^11
        while current > 0:
            if count.get(current, 0) >= 2:
                count[current] -= 2
                count[current - 1] = count.get(current - 1, 0) + 1
            else:
                # Check if we can combine lower powers
                if current - 1 in count and count[current - 1] >= 1:
                    count[current - 1] -= 1
                    count[current - 2] = count.get(current - 2, 0) + 1
                else:
                    break
            current -= 1
        
        if count.get(11, 0) >= 1:
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()