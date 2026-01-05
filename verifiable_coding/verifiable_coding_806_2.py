import sys

def get_first_digit_after_decimal(n, divisor):
    quotient, remainder = divmod(n, divisor)
    if remainder == 0:
        return quotient % 10
    fractional_part = remainder / divisor
    # Convert to string and check first digit after decimal
    fractional_str = str(fractional_part).split('.')[1]
    return int(fractional_str[0])

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        A = int(data[idx])
        B = int(data[idx+1])
        C = int(data[idx+2])
        idx += 3
        Q = int(data[idx])
        idx += 1
        list_ = [N]
        current = N
        for _ in range(10**9):  # enough for the queries
            current = list_[-1]
            # Process A
            digit = get_first_digit_after_decimal(current, A)
            list_.append(digit)
            current = digit
            # Process B
            digit = get_first_digit_after_decimal(current, B)
            list_.append(digit)
            current = digit
            # Process C
            digit = get_first_digit_after_decimal(current, C)
            list_.append(digit)
            current = digit
        for __ in range(Q):
            i = int(data[idx])
            idx += 1
            results.append(str(list_[i]))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()