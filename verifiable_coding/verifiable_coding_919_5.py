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
        
        # Group the sequence into runs of equal elements
        runs = []
        current_val = A[0]
        count = 1
        for i in range(1, N):
            if A[i] == current_val:
                count += 1
            else:
                runs.append(count)
                current_val = A[i]
                count = 1
        runs.append(count)
        
        # Calculate the minimum number of operations
        # We need to make all run lengths even
        # For each run, if it's odd, we need to delete one element or add one element
        # So for each run with odd length, we need 1 operation
        # However, if there is at least one run with even length, we can delete one element from an odd run
        # So the minimum number of operations is the number of runs with odd length
        # But if there is at least one run with even length, we can reduce the count by 1
        odd_runs = sum(1 for run in runs if run % 2 != 0)
        if any(run % 2 == 0 for run in runs):
            results.append(odd_runs - 1)
        else:
            results.append(odd_runs)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()