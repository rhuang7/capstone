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
        # Case 1: do not reverse the array
        # Compute GCD of the entire array
        current_gcd = arr[0]
        for num in arr[1:]:
            current_gcd = int(current_gcd / (current_gcd % num)) if current_gcd % num != 0 else current_gcd
        max_gcd = current_gcd
        # Case 2: reverse the array and compute GCD
        reversed_arr = arr[::-1]
        current_gcd = reversed_arr[0]
        for num in reversed_arr[1:]:
            current_gcd = int(current_gcd / (current_gcd % num)) if current_gcd % num != 0 else current_gcd
        max_gcd = max(max_gcd, current_gcd)
        results.append(max_gcd)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()