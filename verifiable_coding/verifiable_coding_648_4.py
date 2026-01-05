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
        # Find next strictly greater element within 100 distance
        for j in range(i+1, min(i+101, N)):
            if A[j] > A[i]:
                next_greater[i] = j
                break

    def solve():
        for _ in range(Q):
            op = int(data[idx])
            idx += 1
            if op == 1:
                i = int(data[idx]) - 1  # 0-based
                idx += 1
                k = int(data[idx])
                idx += 1
                current = i
                for _ in range(k):
                    if next_greater[current] == 0:
                        break
                    current = next_greater[current]
                print(current + 1)
            elif op == 2:
                L = int(data[idx]) - 1
                idx += 1
                R = int(data[idx]) - 1
                idx += 1
                X = int(data[idx])
                idx += 1
                for i in range(L, R + 1):
                    A[i] += X

if __name__ == '__main__':
    solve()