import sys

def get_first_digit_of_fractional_part(n, divisor):
    quotient, remainder = divmod(n, divisor)
    if remainder == 0:
        return quotient % 10
    fractional_part = remainder / divisor
    # Convert to string to get first digit of fractional part
    fractional_str = str(fractional_part)
    # Find the first non-zero digit in the fractional part
    first_non_zero = None
    for ch in fractional_str:
        if ch != '0':
            first_non_zero = ch
            break
    if first_non_zero is not None:
        return int(first_non_zero)
    # If all are zero, return the first digit of the integral part
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
        for _ in range(10**9):  # Enough steps to cover queries
            current = get_first_digit_of_fractional_part(current, A)
            list_.append(current)
            current = get_first_digit_of_fractional_part(current, B)
            list_.append(current)
            current = get_first_digit_of_fractional_part(current, C)
            list_.append(current)
        for __ in range(Q):
            i = int(input[ptr])
            ptr += 1
            results.append(str(list_[i]))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()