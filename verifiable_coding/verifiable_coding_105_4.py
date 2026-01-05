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
        
        # Sort the array in non-decreasing order
        a.sort()
        
        # Calculate the maximum number of operations
        total = 0
        for i in range(n):
            # Calculate the total candies after adding all previous piles
            total += a[i]
            # Check if the total exceeds k
            if total > k:
                # We can't add this pile, so break
                break
            # The number of operations is the number of previous piles
            total_operations = i
            results.append(total_operations)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()