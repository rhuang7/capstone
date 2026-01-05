import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().decode().strip()
    N = int(input)
    
    count = 0
    
    for num in range(1, N + 1):
        digits = list(map(int, str(num)))
        n = len(digits)
        if n == 1:
            count += 1
            continue
        d = digits[1] - digits[0]
        is_special = True
        for i in range(2, n):
            if digits[i] - digits[i-1] != d:
                is_special = False
                break
        if is_special:
            count += 1
    
    print(count)

if __name__ == '__main__':
    solve()