import sys
import bisect

def main():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    Q = int(data[idx])
    idx += 1
    A = list(map(int, data[idx:idx+N]))
    idx += N

    # Preprocess next greater element for each position
    next_greater = [0] * (N + 2)  # 1-based indexing
    for i in range(N-1, -1, -1):
        # Find next greater element in the next 100 positions
        for j in range(i+1, min(i+101, N)):
            if A[j] > A[i]:
                next_greater[i] = j
                break
        # If no next greater in next 100, set to i
        if next_greater[i] == 0:
            next_greater[i] = i

    def jump(i, k):
        current = i
        for _ in range(k):
            if next_greater[current] == current:
                return current
            current = next_greater[current]
        return current

    def update(L, R, X):
        for i in range(L, R+1):
            A[i-1] += X

    def solve():
        for _ in range(Q):
            op = int(data[idx])
            idx += 1
            if op == 1:
                i = int(data[idx])
                idx += 1
                k = int(data[idx])
                idx += 1
                print(jump(i, k))
            else:
                L = int(data[idx])
                idx += 1
                R = int(data[idx])
                idx += 1
                X = int(data[idx])
                idx += 1
                update(L, R, X)

if __name__ == '__main__':
    solve()