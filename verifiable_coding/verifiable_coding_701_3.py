import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, k = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        prefix_sums = []
        total = 0
        for a in A:
            total += k ** a
            prefix_sums.append(total)
        total = prefix_sums[-1]
        
        max_product = 0
        best_split = 0
        
        for i in range(1, N):
            left = prefix_sums[i-1]
            right = total - left
            product = left * right
            if product > max_product or (product == max_product and i < best_split):
                max_product = product
                best_split = i
        
        results.append(str(best_split))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()