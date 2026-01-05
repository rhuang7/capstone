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
            # This is equivalent to the game of subtraction in the context of the Euclidean algorithm
            # The Grundy number for (a, b) is the same as the number of steps in the Euclidean algorithm
            # when the larger number is divided by the smaller one
            x, y = max(a, b), min(a, b)
            g = 0
            while y != 0:
                g += 1
                x, y = y, x % y
            grundy.append(g)
        # The XOR of all Grundy numbers determines the winner
        xor_sum = 0
        for g in grundy:
            xor_sum ^= g
        if xor_sum != 0:
            results.append("YES")
        else:
            results.append("NO")
    print('\n'.join(results))

if __name__ == '__main__':
    solve()