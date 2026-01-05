import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().decode().split()
    n = int(input[0])
    
    total = 0
    ravi_count = 0
    jhon_count = 0
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            total += i * i
        else:
            total += 2 * i * i
    
    if total % 2 == 0:
        ravi_count += 2
    else:
        jhon_count += 2
    
    if ravi_count > jhon_count:
        print("Ravi")
    else:
        print("Jhon")

if __name__ == '__main__':
    solve()