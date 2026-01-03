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
        xor_val = 0
        for num in a:
            xor_val ^= num
        
        if total_sum == 2 * xor_val:
            results.append("0")
            results.append("")
            continue
        
        # Try to find a solution by adding 1, 2, or 3 elements
        # We'll try to find a value x such that adding x makes the condition true
        # Let's try to find x such that (total_sum + x) = 2 * (xor_val ^ x)
        # This is equivalent to (total_sum + x) = 2 * (xor_val ^ x)
        # We can try small values of x to find a solution
        
        # Try adding one element
        for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            new_sum = total_sum + x
            new_xor = xor_val ^ x
            if new_sum == 2 * new_xor:
                results.append("1")
                results.append(str(x))
                break
        else:
            # Try adding two elements
            for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    new_sum = total_sum + x + y
                    new_xor = xor_val ^ x ^ y
                    if new_sum == 2 * new_xor:
                        results.append("2")
                        results.append(f"{x} {y}")
                        break
                else:
                    continue
                break
            else:
                # Try adding three elements
                for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        for z in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                            new_sum = total_sum + x + y + z
                            new_xor = xor_val ^ x ^ y ^ z
                            if new_sum == 2 * new_xor:
                                results.append("3")
                                results.append(f"{x} {y} {z}")
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()