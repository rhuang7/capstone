import sys

def get_first_digit_of_fraction(x, divisor):
    quotient, remainder = divmod(x, divisor)
    if remainder == 0:
        return quotient % 10
    fractional_part = remainder / divisor
    # Get the first non-zero digit of the fractional part
    digit = 0
    for i in range(1, 10):
        if fractional_part >= 10**(-i):
            digit = i
            break
    return int(fractional_part * 10**digit) % 10

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
        queries = []
        for _ in range(Q):
            queries.append(int(data[idx]))
            idx += 1
        # Initialize list
        lst = [N]
        current = N
        # Repeat the process for A, B, C
        for _ in range(10**9):  # enough to cover all possible queries
            # Process A
            if current == 0:
                lst.append(0)
            else:
                quotient, remainder = divmod(current, A)
                if remainder == 0:
                    lst.append(quotient % 10)
                else:
                    fractional_part = remainder / A
                    digit = 0
                    for i in range(1, 10):
                        if fractional_part >= 10**(-i):
                            digit = i
                            break
                    lst.append(int(fractional_part * 10**digit) % 10)
            current = lst[-1]
            # Process B
            if current == 0:
                lst.append(0)
            else:
                quotient, remainder = divmod(current, B)
                if remainder == 0:
                    lst.append(quotient % 10)
                else:
                    fractional_part = remainder / B
                    digit = 0
                    for i in range(1, 10):
                        if fractional_part >= 10**(-i):
                            digit = i
                            break
                    lst.append(int(fractional_part * 10**digit) % 10)
            current = lst[-1]
            # Process C
            if current == 0:
                lst.append(0)
            else:
                quotient, remainder = divmod(current, C)
                if remainder == 0:
                    lst.append(quotient % 10)
                else:
                    fractional_part = remainder / C
                    digit = 0
                    for i in range(1, 10):
                        if fractional_part >= 10**(-i):
                            digit = i
                            break
                    lst.append(int(fractional_part * 10**digit) % 10)
            current = lst[-1]
            # Check if we have enough elements for queries
            if len(lst) >= max(queries) + 1:
                break
        # Answer queries
        for i in queries:
            results.append(str(lst[i]))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()