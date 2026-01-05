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
        n, k = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Sort the array
        a.sort()
        
        # Calculate the maximum number of operations
        total = 0
        for i in range(n-1, -1, -1):
            if i == n-1:
                # First pile can be used to copy to others
                total += a[i]
            else:
                # Each other pile can be copied to this pile
                total += a[i] * (n - i - 1)
        
        # Subtract the sum of all elements from total
        # Because each operation adds a_i to a_j, which is counted in total
        # But the sum of all elements is the initial sum, and each operation increases the total sum by a_i
        # So the maximum number of operations is (total - sum(a)) // sum(a)
        sum_a = sum(a)
        if sum_a == 0:
            results.append(0)
            continue
        max_ops = (total - sum_a) // sum_a
        results.append(max_ops)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()