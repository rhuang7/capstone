import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        pairs = []
        for _ in range(N):
            a = int(data[idx])
            b = int(data[idx+1])
            idx += 2
            pairs.append((a, b))
        # Calculate Grundy numbers for each pair
        grundy = []
        for a, b in pairs:
            # Compute the Grundy number for the pair (a, b)
            # This is equivalent to the number of times you can subtract the smaller from the larger before they become equal
            # Which is the same as the number of steps in the Euclidean algorithm
            x, y = max(a, b), min(a, b)
            g = 0
            while y != 0:
                g += 1
                x, y = y, x % y
            grundy.append(g)
        # The game is a variant of Nim where each pile has size equal to the Grundy number of the pair
        # The first player wins if the XOR of all Grundy numbers is non-zero
        xor_sum = 0
        for g in grundy:
            xor_sum ^= g
        if xor_sum != 0:
            results.append("YES")
        else:
            results.append("NO")
    print("\n".join(results))

if __name__ == '__main__':
    solve()