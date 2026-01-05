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
        
        # For each position i, find the maximum number of moves starting from i
        # We can use BFS for each position, but that would be O(N^2) which is too slow
        # Instead, we can precompute for each value x, the positions where it occurs
        # Then for each position i, we can jump to i+1 or i+2 if the value is the same
        
        # Preprocess: map each value to a list of indices where it occurs
        value_to_indices = collections.defaultdict(list)
        for i in range(N):
            value_to_indices[a[i]].append(i)
        
        # For each position i, compute the maximum number of moves
        max_moves = 0
        
        for i in range(N):
            current = i
            moves = 0
            visited = set()
            while True:
                if current in visited:
                    break
                visited.add(current)
                # Try to move +1
                if current + 1 < N and a[current + 1] == a[current]:
                    current = current + 1
                    moves += 1
                # Try to move +2
                elif current + 2 < N and a[current + 2] == a[current]:
                    current = current + 2
                    moves += 1
                else:
                    break
            max_moves = max(max_moves, moves)
        
        results.append(str(max_moves))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()