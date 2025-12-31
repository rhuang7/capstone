import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().strip()
    N = int(input)

    special_count = 0
    partial_count = 0

    for num in range(1, 10**6):
        digits = list(map(int, str(num)))
        product = 1
        has_one = False
        for d in digits:
            product *= d
            if d == 1:
                has_one = True
        if product == num:
            if not has_one:
                special_count += 1
            partial_count += 1

    print(special_count, partial_count)

if __name__ == '__main__':
    solve()