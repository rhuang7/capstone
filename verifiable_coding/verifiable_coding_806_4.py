import sys

def get_first_digit_of_fraction(x, divisor):
    quotient, remainder = divmod(x, divisor)
    if remainder == 0:
        return quotient % 10
    fractional_part = remainder / divisor
    # Convert to string and check first digit after decimal
    s = str(fractional_part)
    if '.' in s:
        return int(s.split('.')[1][0])
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
        for _ in range(10**9):  # enough to cover queries up to 1e9
            current = list_[-1]
            # Process A
            quotient, remainder = divmod(current, A)
            if remainder == 0:
                digit = quotient % 10
            else:
                fractional_part = remainder / A
                s = str(fractional_part)
                if '.' in s:
                    digit = int(s.split('.')[1][0])
                else:
                    digit = quotient % 10
            list_.append(digit)
            # Process B
            quotient, remainder = divmod(current, B)
            if remainder == 0:
                digit = quotient % 10
            else:
                fractional_part = remainder / B
                s = str(fractional_part)
                if '.' in s:
                    digit = int(s.split('.')[1][0])
                else:
                    digit = quotient % 10
            list_.append(digit)
            # Process C
            quotient, remainder = divmod(current, C)
            if remainder == 0:
                digit = quotient % 10
            else:
                fractional_part = remainder / C
                s = str(fractional_part)
                if '.' in s:
                    digit = int(s.split('.')[1][0])
                else:
                    digit = quotient % 10
            list_.append(digit)
            # If list is large enough, break to avoid infinite loop
            if len(list_) > 10**9 + 1:
                break
        for _ in range(Q):
            i = int(input[ptr])
            ptr += 1
            results.append(str(list_[i]))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()