import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().decode().strip()
    N = int(input)
    
    count = 0
    
    for length in range(1, len(str(N)) + 1):
        for start in range(0, 10):
            for diff in range(-9, 10):
                num = 0
                valid = True
                for i in range(length):
                    digit = (start + i * diff) % 10
                    if digit < 0:
                        valid = False
                        break
                    num = num * 10 + digit
                if valid and num <= N:
                    count += 1
    
    print(count)

if __name__ == '__main__':
    solve()