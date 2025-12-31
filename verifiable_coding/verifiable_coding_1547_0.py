import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    D1 = int(data[0])
    V1 = int(data[1])
    D2 = int(data[2])
    V2 = int(data[3])
    P = int(data[4])

    total = 0
    days = 0

    while total < P:
        days += 1
        if days >= D1 and days >= D2:
            total += V1 + V2
        elif days >= D1:
            total += V1
        elif days >= D2:
            total += V2
        # else: no production

    print(days)

if __name__ == '__main__':
    solve()