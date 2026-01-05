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
                # Try adding 2^i
                new_sum = total_sum + (1 << i)
                new_xor = xor_sum ^ (1 << i)
                if new_sum == 2 * new_xor:
                    results.append("1")
                    results.append(str(1 << i))
                    found = True
                    break
        if found:
            continue
        # Try to find two elements to add
        for i in range(63):
            if (xor_sum >> i) & 1:
                # Try adding 2^i and 2^i
                new_sum = total_sum + 2 * (1 << i)
                new_xor = xor_sum ^ (1 << i) ^ (1 << i)
                if new_sum == 2 * new_xor:
                    results.append("2")
                    results.append(str(1 << i) + " " + str(1 << i))
                    found = True
                    break
        if found:
            continue
        # Try to find three elements to add
        for i in range(63):
            if (xor_sum >> i) & 1:
                # Try adding 2^i, 2^i, 2^i
                new_sum = total_sum + 3 * (1 << i)
                new_xor = xor_sum ^ (1 << i) ^ (1 << i) ^ (1 << i)
                if new_sum == 2 * new_xor:
                    results.append("3")
                    results.append(str(1 << i) + " " + str(1 << i) + " " + str(1 << i))
                    found = True
                    break
        if not found:
            # Fallback to adding 4 and 4
            results.append("2")
            results.append("4 4")
    print("\n".join(results))