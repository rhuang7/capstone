import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    N = int(data[0])
    A = list(map(int, data[1:]))
    
    prefix_sum = 0
    sum_count = {}
    sum_count[0] = 1
    result = 0
    
    for num in A:
        prefix_sum += num
        if prefix_sum in sum_count:
            result += sum_count[prefix_sum]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    print(result)

if __name__ == '__main__':
    solve()