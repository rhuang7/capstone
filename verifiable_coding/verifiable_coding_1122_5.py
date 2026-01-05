import sys

def solve():
    import sys
    input = sys.stdin.buffer.read().split()
    n = int(input[0])
    
    sum_series = 0
    ravi_count = 0
    jhon_count = 0
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            sum_series += i * i
        else:
            sum_series += 2 * i * i
    
    if sum_series % 2 == 0:
        ravi_count += 2
    else:
        jhon_count += 2
    
    if ravi_count > jhon_count:
        print("Ravi")
    else:
        print("Jhon")

if __name__ == '__main__':
    solve()