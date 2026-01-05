import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    A = list(map(int, data[1:]))

    # Check for any 4 consecutive elements
    for i in range(n - 3):
        a = A[i]
        b = A[i + 1]
        c = A[i + 2]
        d = A[i + 3]
        if (a ^ b ^ c ^ d) == 0:
            print("Yes")
            return

    # Check for any 4 elements with a pattern
    # Since the sequence is similar to Gray code, check for patterns
    # If there are 4 elements with alternating bits, then the XOR can be 0
    # If there are 4 elements with two pairs of equal values, then XOR can be 0
    # If there are 4 elements with two pairs of values that XOR to 0, then XOR can be 0
    # Check for any 4 elements with XOR 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if (A[i] ^ A[j] ^ A[k] ^ A[l]) == 0:
                        print("Yes")
                        return

    print("No")

if __name__ == '__main__':
    solve()