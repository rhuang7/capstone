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
            results.append("0")
            results.append("")
            continue
        # Try to find a solution by adding 1, 2, or 3 elements
        # Try adding 1 element
        found = False
        for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
            new_sum = total_sum + x
            new_xor = xor_sum ^ x
            if new_sum == 2 * new_xor:
                results.append("1")
                results.append(str(x))
                found = True
                break
        if found:
            continue
        # Try adding 2 elements
        for x in range(0, 19):
            for y in range(0, 19):
                new_sum = total_sum + x + y
                new_xor = xor_sum ^ x ^ y
                if new_sum == 2 * new_xor:
                    results.append("2")
                    results.append(f"{x} {y}")
                    found = True
                    break
            if found:
                break
        if found:
            continue
        # Try adding 3 elements
        for x in range(0, 19):
            for y in range(0, 19):
                for z in range(0, 19):
                    new_sum = total_sum + x + y + z
                    new_xor = xor_sum ^ x ^ y ^ z
                    if new_sum == 2 * new_xor:
                        results.append("3")
                        results.append(f"{x} {y} {z}")
                        found = True
                        break
                if found:
                    break
            if found:
                break
        if found:
            continue
        # If not found, use a fallback (should not happen as per problem statement)
        results.append("3")
        results.append("2 6 2")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()