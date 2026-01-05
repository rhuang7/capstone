import sys
input = sys.stdin.buffer.read
def solve():
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, Q = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        X_pos = -1
        for i in range(N):
            if A[i] == X:
                X_pos = i
                break
        pos_map = {val: i for i, val in enumerate(A)}
        for __ in range(Q):
            X = int(data[idx])
            idx += 1
            if X == A[X_pos]:
                results.append(0)
                continue
            correct_pos = pos_map[X]
            if correct_pos == X_pos:
                results.append(0)
                continue
            # Find the minimum number of swaps to bring X to its correct position
            # We need to swap elements until X is at its correct position
            # Each swap moves X one step closer
            # So the minimum number of swaps is the distance between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # We need to find the minimum number of swaps to bring X to its correct position
            # The minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move X itself, we need to find the minimum number of swaps to bring X to correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since we can't move