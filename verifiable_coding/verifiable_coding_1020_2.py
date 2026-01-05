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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # We need to find the maximum possible absolute value of the expression
        # when both players play optimally. Vanja wants to maximize |V|, Miksi to minimize it.
        
        # We can use dynamic programming to track the possible values of the expression
        # at each step. Since the values can be large, we'll use a set to track possible values.
        
        # Initialize the possible values with the first element
        possible = {A[0]}
        
        for i in range(1, N):
            new_possible = set()
            for val in possible:
                new_possible.add(val + A[i])
                new_possible.add(val - A[i])
            possible = new_possible
        
        max_abs = max(abs(x) for x in possible)
        if max_abs >= K:
            results.append(1)
        else:
            results.append(2)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()