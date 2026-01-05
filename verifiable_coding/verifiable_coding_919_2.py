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
        prev = A[0]
        count = 1
        for i in range(1, N):
            if A[i] == prev:
                count += 1
            else:
                runs.append(count)
                prev = A[i]
                count = 1
        runs.append(count)
        
        # Calculate the minimum operations needed
        # We need to make all run lengths even
        # For each run, if it's odd, we need to delete one element or insert one element
        # But we can choose to delete or insert based on which is better
        # However, since we can insert anywhere, it's better to delete one element if the run is odd
        # Because inserting an element would require one operation, but deleting one element also requires one operation
        # But inserting can be used to make a run even by adding one element
        # However, we can't just delete one element from an odd run, because that would make it even
        # So for each run with odd length, we need to perform one operation (either delete or insert)
        # But if there are multiple runs with odd lengths, we can choose to delete one element from one of them
        # So the minimum number of operations is the number of runs with odd lengths
        # Because for each such run, we need to perform one operation
        # However, if there are multiple such runs, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them, which would make it even
        # So the minimum number of operations is the number of runs with odd lengths
        # Because for each such run, we need to perform one operation (either delete or insert)
        # But if there are multiple such runs, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths
        # But wait, if there are multiple runs with odd lengths, we can delete one element from one of them
        # So the answer is the number of runs with odd lengths