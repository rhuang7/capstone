import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    
    total = 0
    ravi = 0
    jhon = 0
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            total += i * i
        else:
            total += 2 * (i * i)
    
    if total % 2 == 0:
        ravi += 2
    else:
        jhon += 2
    
    if ravi > jhon:
        print("Ravi")
    else:
        print("Jhon")

if __name__ == '__main__':
    solve()