import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    D1, V1, D2, V2, P = map(int, input)
    
    total = 0
    days = 0
    
    while True:
        days += 1
        if days >= D1 and days >= D2:
            total += V1 + V2
        elif days >= D1:
            total += V1
        elif days >= D2:
            total += V2
        else:
            total += 0
        
        if total >= P:
            print(days)
            break

if __name__ == '__main__':
    solve()