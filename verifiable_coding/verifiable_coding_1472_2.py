import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().strip()
    N = int(input)

    def is_special(num):
        digits = list(map(int, str(num)))
        product = 1
        for d in digits:
            product *= d
        return product == num

    def count_special_numbers(limit):
        special_count = 0
        partial_count = 0
        for num in range(1, limit + 1):
            if is_special(num):
                special_count += 1
            if is_special(num) or '1' in str(num):
                partial_count += 1
        return special_count, partial_count

    special, partial = count_special_numbers(N)
    print(f"{special} {partial}")

if __name__ == '__main__':
    solve()