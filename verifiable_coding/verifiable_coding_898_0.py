import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        M = int(data[index])
        N = int(data[index + 1])
        index += 2
        
        count_pairs = 0
        count_x = 0
        
        for x in range(1, M + 1):
            for y in range(1, N + 1):
                product = x * y
                sum_xy = x + y
                total = product + sum_xy
                s = str(x) + str(y)
                if str(total) == s:
                    count_pairs += 1
                    count_x += 1
        
        results.append(f"{count_pairs} {count_x}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()