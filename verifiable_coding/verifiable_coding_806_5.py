import sys

def get_first_digit_of_fraction(x, divisor):
    quotient, remainder = divmod(x, divisor)
    if remainder == 0:
        return quotient % 10
    fractional_part = remainder / divisor
    # Get the first non-zero digit of the fractional part
    digit = 0
    while fractional_part > 0:
        fractional_part *= 10
        digit = int(fractional_part)
        if digit != 0:
            break
    return digit

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
        for _ in range(3):  # A, B, C
            if current == 0:
                list_.append(0)
                current = 0
            else:
                if _ == 0:
                    divisor = A
                elif _ == 1:
                    divisor = B
                else:
                    divisor = C
                quotient, remainder = divmod(current, divisor)
                if remainder == 0:
                    digit = quotient % 10
                else:
                    fractional_part = remainder / divisor
                    digit = 0
                    while fractional_part > 0:
                        fractional_part *= 10
                        digit = int(fractional_part)
                        if digit != 0:
                            break
                list_.append(digit)
                current = digit
        for _ in range(Q):
            i = int(data[idx])
            idx += 1
            results.append(str(list_[i]))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()