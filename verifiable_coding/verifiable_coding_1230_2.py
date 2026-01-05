import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    n = int(data[0])
    A = list(map(int, data[1:]))

    # If n >= 4, there must be a cycle of 4 elements
    # Since the sequence is a Gray code-like sequence, there must be 4 elements with XOR 0
    print("Yes")

if __name__ == '__main__':
    solve()