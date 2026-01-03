import sys

def get_first_digit_of_fraction(x, divisor):
    quotient, remainder = divmod(x, divisor)
    if remainder == 0:
        return quotient % 10
    fractional_part = remainder / divisor
    # Convert to string to find first non-zero digit
    fractional_str = str(fractional_part)
    for c in fractional_str:
        if c != '0':
            return int(c)
    return quotient % 10

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    results = []
    for _ in range(T):
        N = int(input[ptr])
        ptr += 1
        A = int(input[ptr])
        B = int(input[ptr+1])
        C = int(input[ptr+2])
        ptr += 3
        Q = int(input[ptr])
        ptr += 1
        list_ = [N]
        current = N
        for _ in range(10**9):  # enough steps for all queries
            current = list_[-1]
            if A:
                first_digit = get_first_digit_of_fraction(current, A)
                list_.append(first_digit)
            if B:
                first_digit = get_first_digit_of_fraction(current, B)
                list_.append(first_digit)
            if C:
                first_digit = get_first_digit_of_fraction(current, C)
                list_.append(first_digit)
            # Stop after 10^9 steps (as per query constraints)
            if len(list_) > 10**9 + 1:
                break
        for _ in range(Q):
            i = int(input[ptr])
            ptr += 1
            results.append(str(list_[i]))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()