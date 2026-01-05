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
        N = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        
        max_gcd = 0
        # Case 1: Do not reverse the array
        # Compute GCD of the entire array
        current_gcd = arr[0]
        for num in arr[1:]:
            current_gcd = (current_gcd * num) // (current_gcd % num)
            if current_gcd == 0:
                break
        max_gcd = current_gcd
        
        # Case 2: Reverse the array
        # Compute GCD of the entire array
        current_gcd = arr[-1]
        for num in arr[:-1]:
            current_gcd = (current_gcd * num) // (current_gcd % num)
            if current_gcd == 0:
                break
        max_gcd = max(max_gcd, current_gcd)
        
        results.append(max_gcd)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()