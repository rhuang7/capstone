import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    prefix_sum = 0
    sum_counts = {}
    sum_counts[0] = 1
    count = 0
    
    for num in A:
        prefix_sum += num
        if prefix_sum in sum_counts:
            count += sum_counts[prefix_sum]
        else:
            sum_counts[prefix_sum] = 1
    
    print(count)

if __name__ == '__main__':
    solve()