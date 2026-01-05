import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    T = int(input[0])
    cases = list(map(int, input[1:T+1]))
    
    for k in cases:
        # Generate the alphabetic part
        alphabets = ''.join([chr(ord('A') + i) for i in range(k)])
        # Generate the numeric part
        numbers = ''.join(map(str, range(1, k+1)))
        # Print the pattern
        print(alphabets)
        print(numbers)
        
if __name__ == '__main__':
    solve()