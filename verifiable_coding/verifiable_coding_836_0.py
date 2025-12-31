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
        n = int(data[idx])
        idx += 1
        L = list(map(int, data[idx:idx+n]))
        idx += n
        R = list(map(int, data[idx:idx+n]))
        idx += n
        
        max_product = -1
        max_rating = -1
        best_index = -1
        
        for i in range(n):
            product = L[i] * R[i]
            if product > max_product or (product == max_product and R[i] > max_rating) or (product == max_product and R[i] == max_rating and i < best_index):
                max_product = product
                max_rating = R[i]
                best_index = i + 1  # 1-based index
        
        results.append(str(best_index))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()