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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        total = sum(A)
        # The sum of the sequence can be adjusted by subtracting i * k for each element
        # The total sum after operations is sum(A_i - i * k_i) = sum(A_i) - sum(i * k_i)
        # We need sum(A_i) - sum(i * k_i) = 0 => sum(i * k_i) = sum(A_i)
        # Since k_i can be any non-negative integer, we can choose k_i such that sum(i * k_i) = sum(A_i)
        # This is always possible if sum(A_i) is non-negative and we can distribute the sum among the i's
        # However, since we can subtract any multiple of i, the key is that sum(A_i) must be achievable as a sum of multiples of i's
        # But since we can choose any number of operations, we can always achieve any non-negative sum
        # So the answer is YES if sum(A_i) is non-negative, otherwise NO
        if total >= 0:
            results.append("YES")
        else:
            results.append("NO")
    print("\n".join(results))

if __name__ == '__main__':
    solve()