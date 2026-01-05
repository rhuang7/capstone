import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    for i in range(1, T + 1):
        K = int(input[i])
        # Generate the alphabetic part
        alphabets = ''
        for j in range(1, K + 1):
            alphabets += chr(ord('A') + j - 1)
        # Generate the numeric part
        numbers = ''
        for j in range(1, K + 1):
            numbers += str(j)
        # Print the pattern
        print(alphabets)
        print(numbers)

if __name__ == '__main__':
    solve()