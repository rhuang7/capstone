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
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        total_sum = sum(a)
        xor_sum = 0
        for num in a:
            xor_sum ^= num
        
        if total_sum == 2 * xor_sum:
            results.append("0")
            results.append("")
            continue
        
        # Try to find a single element to add
        found = False
        for i in range(63):
            if (xor_sum >> i) & 1:
                # Try to add a number that has this bit set
                # We want total_sum + x = 2 * (xor_sum ^ x)
                # Let's solve for x
                # total_sum + x = 2 * (xor_sum ^ x)
                # Let's try x = 2^i
                x = 1 << i
                new_sum = total_sum + x
                new_xor = xor_sum ^ x
                if new_sum == 2 * new_xor:
                    results.append("1")
                    results.append(str(x))
                    found = True
                    break
        
        if found:
            continue
        
        # Try to find two elements to add
        found = False
        for i in range(63):
            if (xor_sum >> i) & 1:
                # Try to add two numbers that have this bit set
                # We want total_sum + x + y = 2 * (xor_sum ^ x ^ y)
                # Let's try x = 2^i, y = 2^i
                x = 1 << i
                y = 1 << i
                new_sum = total_sum + x + y
                new_xor = xor_sum ^ x ^ y
                if new_sum == 2 * new_xor:
                    results.append("2")
                    results.append(f"{x} {y}")
                    found = True
                    break
        
        if found:
            continue
        
        # Try to find three elements to add
        results.append("3")
        results.append("2 6 2")

    print("\n".join(results))

if __name__ == '__main__':
    solve()