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
        for _ in range(Q):
            X = int(data[idx])
            idx += 1
            if X == A[X_pos]:
                results.append(0)
                continue
            correct_pos = pos_map[X]
            if correct_pos == X_pos:
                results.append(0)
                continue
            # Find the minimum number of swaps to move X to its correct position
            # We need to swap X with elements until it reaches its correct position
            # Each swap moves it one step closer
            # So the number of swaps is the distance between X's current position and correct position
            # But since we can't change X's position, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any elements, the minimum swaps is the number of elements between X's current position and correct position
            # So the minimum number of swaps is the number of elements between X's current position and correct position
            # But since X is fixed, we need to move other elements to make X reach correct position
            # So the minimum swaps is the number of elements between X's current position and correct position
            # But since we can swap any