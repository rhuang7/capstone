import sys

def is_ciel_number(k):
    count = [0] * 10
    for ch in str(k):
        digit = int(ch)
        count[digit] += 1
    d8 = count[8]
    d5 = count[5]
    d3 = count[3]
    for i in range(0, 3, 1):
        if count[i] > 0:
            return False
    return d8 >= d5 >= d3

def solve():
    import sys
    input = sys.stdin.buffer.read().split(b'\n')
    n = int(input[0])
    count = 0
    for line in input[1:n+1]:
        if not line:
            continue
        parts = line.split(b' ')
        if len(parts) < 2:
            continue
        name = parts[0]
        price = int(parts[1])
        if is_ciel_number(price):
            count += 1
    print(count)

if __name__ == '__main__':
    solve()