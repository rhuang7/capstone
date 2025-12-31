import sys

def is_ciel_number(p):
    count = [0] * 10
    for c in p:
        if c.isdigit():
            count[int(c)] += 1
    d8 = count[8]
    d5 = count[5]
    d3 = count[3]
    for i in range(0, 3, 1):
        if i == 0 or i == 1 or i == 2 or i == 4 or i == 6 or i == 7 or i == 9:
            if count[i] > 0:
                return False
    return d8 >= d5 >= d3

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split(b'\n')
    N = int(data[0])
    count = 0
    for line in data[1:N+1]:
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