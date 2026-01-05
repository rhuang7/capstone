import sys

def solve():
    import sys
    D1, V1, D2, V2, P = map(int, sys.stdin.buffer.read().split())
    
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
        else:
            pass
    print(days)

if __name__ == '__main__':
    solve()