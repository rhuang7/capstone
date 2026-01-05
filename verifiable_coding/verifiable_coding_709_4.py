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
        # Try all possible subarrays to remove
        # But since we can remove any subarray, the remaining elements are the ones not in the subarray
        # So the maximum GCD is the maximum GCD of all possible subsets of the array
        # However, this is not feasible for large N
        # So we use a better approach
        # The maximum possible GCD is the maximum element in the array
        # Because if we remove all elements except one, the GCD is that element
        # So the maximum possible GCD is the maximum element in the array
        # But we can also reverse the array, so the maximum possible GCD is the maximum of the maximum element and the maximum element after reversing
        # But reversing the array doesn't change the maximum element
        max_gcd = max(arr)
        # Case 2: reverse the array
        # The maximum possible GCD is the same as before
        results.append(str(max_gcd))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()