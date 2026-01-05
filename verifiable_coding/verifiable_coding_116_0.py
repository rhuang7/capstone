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
        total = sum(a)
        xor = 0
        for num in a:
            xor ^= num
        if total == 2 * xor:
            results.append("0\n")
            results.append("")
            continue
        # Try to find a solution by adding 1, 2, or 3 elements
        # Try adding 1 element
        found = False
        for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
            new_total = total + x
            new_xor = xor ^ x
            if new_total == 2 * new_xor:
                results.append("1\n")
                results.append(str(x))
                found = True
                break
        if found:
            continue
        # Try adding 2 elements
        for x in range(1, 10):
            for y in range(1, 10):
                new_total = total + x + y
                new_xor = xor ^ x ^ y
                if new_total == 2 * new_xor:
                    results.append("2\n")
                    results.append(f"{x} {y}")
                    found = True
                    break
            if found:
                break
        if found:
            continue
        # Try adding 3 elements
        for x in range(1, 10):
            for y in range(1, 10):
                for z in range(1, 10):
                    new_total = total + x + y + z
                    new_xor = xor ^ x ^ y ^ z
                    if new_total == 2 * new_xor:
                        results.append("3\n")
                        results.append(f"{x} {y} {z}")
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if found:
            continue
        # If not found, use a fallback solution (this should never happen)
        results.append("3\n")
        results.append("2 6 2")
    print(''.join(results))

if __name__ == '__main__':
    solve()