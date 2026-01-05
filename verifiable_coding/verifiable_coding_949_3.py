import sys
import collections

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
        a = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Preprocess: for each value, store the indices where it appears
        pos = collections.defaultdict(list)
        for i in range(N):
            pos[a[i]].append(i)
        
        max_moves = 0
        
        # For each position i, find the maximum number of moves starting from i
        for i in range(N):
            current = a[i]
            moves = 0
            j = i
            while True:
                # Check if we can move +1
                if j + 1 < N and a[j + 1] == current:
                    j += 1
                    moves += 1
                # Check if we can move +2
                elif j + 2 < N and a[j + 2] == current:
                    j += 2
                    moves += 1
                else:
                    break
            max_moves = max(max_moves, moves)
        
        results.append(str(max_moves))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()