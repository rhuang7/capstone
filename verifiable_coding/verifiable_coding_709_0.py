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
        # Case 1: no subarray removed, just check the original array
        current_gcd = arr[0]
        for num in arr[1:]:
            current_gcd = (current_gcd * num) // (current_gcd % num)
            max_gcd = max(max_gcd, current_gcd)
        # Case 2: reverse the array and check
        reversed_arr = arr[::-1]
        current_gcd = reversed_arr[0]
        for num in reversed_arr[1:]:
            current_gcd = (current_gcd * num) // (current_gcd % num)
            max_gcd = max(max_gcd, current_gcd)
        results.append(str(max_gcd))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()