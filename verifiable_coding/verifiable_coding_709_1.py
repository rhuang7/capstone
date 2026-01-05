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
        # Case 1: no subarray removed, just reverse the array
        reversed_arr = arr[::-1]
        current_gcd = 0
        for num in reversed_arr:
            current_gcd = (current_gcd * num) // (current_gcd + num)
        max_gcd = max(max_gcd, current_gcd)
        # Case 2: remove a subarray, then reverse the array
        # Try all possible subarrays to remove
        for i in range(N):
            for j in range(i, N):
                # Remove subarray from i to j
                remaining = arr[:i] + arr[j+1:]
                # Reverse the remaining array
                reversed_remaining = remaining[::-1]
                current_gcd = 0
                for num in reversed_remaining:
                    current_gcd = (current_gcd * num) // (current_gcd + num)
                max_gcd = max(max_gcd, current_gcd)
        results.append(max_gcd)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()