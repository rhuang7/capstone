import sys

def get_first_digit_of_fraction(x, divisor):
    quotient, remainder = divmod(x, divisor)
    if remainder == 0:
        return quotient % 10
    decimal_part = remainder / divisor
    # Get the first non-zero digit of the fractional part
    digit = 0
    for i in range(1, 10):
        if decimal_part >= 10**(-i):
            digit = i
            break
    return int(str(decimal_part)[digit])

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        N = int(input[ptr])
        ptr += 1
        A = int(input[ptr])
        B = int(input[ptr+1])
        C = int(input[ptr+2])
        ptr += 3
        Q = int(input[ptr])
        ptr += 1
        queries = []
        for __ in range(Q):
            queries.append(int(input[ptr]))
            ptr += 1
        
        # Generate the list
        lst = [N]
        current = N
        for _ in range(10**9):  # Enough steps for the queries
            if len(lst) > 10**9:
                break
            current = lst[-1]
            if A:
                val = current / A
                if val.is_integer():
                    lst.append(int(val) % 10)
                else:
                    first_digit = get_first_digit_of_fraction(current, A)
                    lst.append(first_digit)
            if B:
                val = current / B
                if val.is_integer():
                    lst.append(int(val) % 10)
                else:
                    first_digit = get_first_digit_of_fraction(current, B)
                    lst.append(first_digit)
            if C:
                val = current / C
                if val.is_integer():
                    lst.append(int(val) % 10)
                else:
                    first_digit = get_first_digit_of_fraction(current, C)
                    lst.append(first_digit)
        
        for i in queries:
            print(lst[i])

if __name__ == '__main__':
    solve()