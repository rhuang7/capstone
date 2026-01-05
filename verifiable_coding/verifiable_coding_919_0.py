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
        
        # Calculate the minimum operations needed
        # For each run, if its length is odd, we need to delete one element or insert one element
        # To minimize operations, we can delete one element from the run (cost 1) or insert one (cost 1)
        # But if we have multiple runs with odd lengths, we can delete one element from two runs (cost 2)
        # So the minimum number of operations is the number of runs with odd lengths, if it's even, else it's (number of odd runs + 1)
        odd_count = sum(1 for r in runs if r % 2 != 0)
        if odd_count % 2 == 0:
            res = odd_count
        else:
            res = odd_count + 1
        
        results.append(res)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()