import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().decode().strip()
    N = int(input)
    
    special = 0
    partial = 0
    
    for num in range(1, 10**6):
        digits = list(map(int, str(num)))
        product = 1
        for d in digits:
            product *= d
        if product == num:
            if 1 not in digits:
                special += 1
            else:
                partial += 1
    
    print(special, partial)

if __name__ == '__main__':
    solve()