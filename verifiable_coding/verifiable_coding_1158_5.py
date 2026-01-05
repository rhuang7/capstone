import sys

def is_ciel_number(p):
    count = [0] * 10
    for c in p:
        if c.isdigit():
            count[int(c)] += 1
    d8 = count[8]
    d5 = count[5]
    d3 = count[3]
    for i in range(0, 3):
        if i != 3 and i != 5 and i != 8:
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
        price = parts[1]
        if is_ciel_number(price):
            count += 1
    print(count)

if __name__ == '__main__':
    solve()