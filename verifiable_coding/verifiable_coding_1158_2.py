import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    N = int(input[0])
    count = 0
    for line in input[1:N+1]:
        if not line:
            continue
        parts = line.split(b' ')
        if len(parts) < 2:
            continue
        name = parts[0]
        Pi = parts[1]
        if not Pi.isdigit():
            continue
        Pi = int(Pi)
        digits = list(str(Pi))
        count_8 = digits.count('8')
        count_5 = digits.count('5')
        count_3 = digits.count('3')
        if count_8 >= count_5 >= count_3:
            count += 1
    print(count)

if __name__ == '__main__':
    solve()