import sys

def solve():
    data = sys.stdin.buffer.read().decode().strip()
    calories = 0
    for ch in data:
        if ch == 'D':
            calories += 238
        elif ch == 'T':
            calories += 244
        elif ch == 'M':
            calories += 138
        elif ch == 'B':
            calories += 279
        elif ch == 'C':
            calories += 186

    total = 0
    ran = 0
    cycled = 0
    walked = 0

    # Prioritize running
    ran = calories // 50
    remaining = calories % 50
    total += ran * 50

    # Prioritize cycling
    cycled = remaining // 5
    remaining %= 5
    total += cycled * 5

    # Walk the rest
    walked = remaining / 0.5

    print(ran)
    print(cycled)
    print(walked)

if __name__ == '__main__':
    solve()