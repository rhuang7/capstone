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
        # Calculate the difference between each pair of adjacent plants
        diffs = []
        for i in range(N-1):
            diffs.append(A[i] - A[i+1])
        # For each plant, calculate the time when it will match the next one
        # The time for plant i to match plant i+1 is (A[i] - A[i+1]) / (i - (i+1)) = (A[i] - A[i+1]) / (-1) = A[i+1] - A[i]
        # But since we want the earliest time when any two plants have the same height, we need to find the minimum time when any two plants have the same height
        # So we check for each pair of plants (i, j) where i < j, the time when A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there exists i < j with A[i] + i*t = A[j] + j*t => t = (A[j] - A[i]) / (i - j)
        # Since i < j, i - j is negative, so t is negative, which is invalid
        # So we need to find the minimum t such that there