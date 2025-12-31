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
        a = list(map(int, data[idx:idx + n]))
        idx += n
        
        total_sum = sum(a)
        xor_sum = 0
        for num in a:
            xor_sum ^= num
        
        if total_sum == 2 * xor_sum:
            results.append("0\n")
            results.append("")
            continue
        
        # Try to find a single element to add
        found = False
        for i in range(63):
            if (xor_sum >> i) & 1:
                # Try to set this bit to 0
                new_xor = xor_sum ^ (1 << i)
                new_sum = total_sum + (1 << i)
                if new_sum == 2 * new_xor:
                    results.append("1\n")
                    results.append(str(1 << i))
                    found = True
                    break
        
        if found:
            continue
        
        # Try to find two elements to add
        for i in range(63):
            if (xor_sum >> i) & 1:
                # Try to set this bit to 0
                new_xor = xor_sum ^ (1 << i)
                new_sum = total_sum + (1 << i)
                if new_sum == 2 * new_xor:
                    results.append("1\n")
                    results.append(str(1 << i))
                    found = True
                    break
        
        if found:
            continue
        
        # Try to find three elements to add
        # Try adding 0, 0, 0
        results.append("3\n")
        results.append("0 0 0")
    
    print(''.join(results))

if __name__ == '__main__':
    solve()