import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        if N == 1:
            results.append("Grinch")
            continue
        # Check if N is even
        if N % 2 == 0:
            # If N is even, subtract 1 to make it odd
            results.append("Me")
        else:
            # If N is odd, check if it's a prime
            is_prime = True
            for j in range(3, int(N**0.5) + 1, 2):
                if N % j == 0:
                    is_prime = False
                    break
            if is_prime:
                # If N is a prime, subtract 1
                results.append("Me")
            else:
                # If N is composite and odd, divide by an odd divisor > 1
                # Since it's composite, it has at least one odd divisor > 1
                results.append("Me")
    print("\n".join(results))

if __name__ == '__main__':
    solve()