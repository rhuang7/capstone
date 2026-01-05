import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        # Generate the alphabetic part
        alphabets = ''
        for i in range(1, k+1):
            alphabets += chr(ord('A') + i - 1)
        # Generate the numeric part
        numbers = ''
        for i in range(1, k+1):
            numbers += str(i)
        # Print the pattern
        print(alphabets)
        print(numbers)

if __name__ == '__main__':
    solve()