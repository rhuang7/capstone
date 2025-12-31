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

    running = 0
    cycling = 0
    walking = 0

    # Try to use running first
    running = calories // 50
    remaining = calories % 50

    # Try to use cycling next
    cycling = remaining // 5
    remaining %= 5

    # Use walking for the remaining
    walking = remaining / 0.5

    print(running)
    print(cycling)
    print(walking)

if __name__ == '__main__':
    solve()