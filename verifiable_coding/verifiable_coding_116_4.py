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
        xor_val = 0
        for num in a:
            xor_val ^= num
        
        if total_sum == 2 * xor_val:
            results.append("0")
            results.append("")
            continue
        
        # Try to find a single element to add
        for i in range(32):
            mask = 1 << i
            if (total_sum ^ (2 * xor_val)) & mask:
                # Try adding mask
                new_sum = total_sum + mask
                new_xor = xor_val ^ mask
                if new_sum == 2 * new_xor:
                    results.append("1")
                    results.append(str(mask))
                    break
        else:
            # Try to find two elements to add
            for i in range(32):
                mask1 = 1 << i
                if (total_sum ^ (2 * xor_val)) & mask1:
                    for j in range(i, 32):
                        mask2 = 1 << j
                        new_sum = total_sum + mask1 + mask2
                        new_xor = xor_val ^ mask1 ^ mask2
                        if new_sum == 2 * new_xor:
                            results.append("2")
                            results.append(f"{mask1} {mask2}")
                            break
                    else:
                        continue
                    break
            else:
                # Try to find three elements to add
                for i in range(32):
                    mask1 = 1 << i
                    if (total_sum ^ (2 * xor_val)) & mask1:
                        for j in range(i, 32):
                            mask2 = 1 << j
                            if (total_sum ^ (2 * xor_val)) & mask2:
                                for k in range(j, 32):
                                    mask3 = 1 << k
                                    new_sum = total_sum + mask1 + mask2 + mask3
                                    new_xor = xor_val ^ mask1 ^ mask2 ^ mask3
                                    if new_sum == 2 * new_xor:
                                        results.append("3")
                                        results.append(f"{mask1} {mask2} {mask3}")
                                        break
                                else:
                                    continue
                                break
                        else:
                            continue
                        break

    print("\n".join(results))

if __name__ == '__main__':
    solve()