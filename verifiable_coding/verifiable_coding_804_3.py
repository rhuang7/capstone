import sys
import math

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
        A = list(map(int, data[idx:idx + N - 1]))
        idx += N - 1
        F = int(data[idx])
        idx += 1
        
        # Find the minimum D and position P such that Josh survives
        possible = False
        min_D = float('inf')
        best_P = -1
        
        # Try all possible positions P for Josh
        for P in range(1, N + 1):
            # Create the circular array with Josh's position P
            # The order is 1, 2, ..., P-1, N, P, P+1, ..., N-1
            # So the array is [A[0], A[1], ..., A[P-2], A[N-1], A[P-1], A[P], ..., A[N-2]]
            # But since A has N-1 elements, we need to adjust
            # Let's create the circular array
            # The soldiers are in the order: 1, 2, ..., P-1, N, P, P+1, ..., N-1
            # So the array is:
            # [A[0], A[1], ..., A[P-2], A[N-1], A[P-1], A[P], ..., A[N-2]]
            # But since A has N-1 elements, A[N-1] is the last element
            # So the array is:
            # [A[0], A[1], ..., A[P-2], A[N-1], A[P-1], A[P], ..., A[N-2]]
            # Let's create this array
            # For P = 1, the order is [N, 1, 2, ..., N-1]
            # For P = N, the order is [1, 2, ..., N-1, N]
            # So the array is:
            # If P == 1: [A[N-1], A[0], A[1], ..., A[N-2]]
            # Else: [A[0], A[1], ..., A[P-2], A[N-1], A[P-1], A[P], ..., A[N-2]]
            if P == 1:
                arr = [A[N-1]] + A[:N-1]
            else:
                arr = A[:P-1] + [A[N-1]] + A[P-1:N-1]
            
            # Now simulate the suicide process
            # The initial attacking soldier is 1 (index 0 in arr)
            # We need to find the order of attacks and calculate the total damage Josh takes
            # We can simulate this with a list of alive soldiers
            alive = list(range(N))
            current = 0  # index of the attacking soldier
            total_damage = 0
            
            # Simulate the process until there are 2 soldiers left
            while len(alive) > 2:
                # The attacking soldier is alive[current]
                # The next soldier is (current + 1) % len(alive)
                next_attacker = (current + 1) % len(alive)
                # The attacked soldier is alive[next_attacker]
                # The attacker is alive[current]
                # The attacked soldier dies
                attacked = alive[next_attacker]
                # If the attacked is Josh (P), then he defends
                if attacked == P - 1:  # since arr is 0-based, P-1 is the index of Josh
                    total_damage += A[attacked]  # A[attacked] is the power of the attacker
                # Remove the attacked soldier from the list
                alive.pop(next_attacker)
                # The next attacker is the next soldier to the right of the current attacker
                current = next_attacker
            
            # Now there are 2 soldiers left
            # Check if Josh is one of them
            if P - 1 in alive:
                # The other soldier is alive[0] if P-1 is alive[1], or alive[1] if P-1 is alive[0]
                other = alive[0] if alive[1] == P - 1 else alive[1]
                # Check if the other soldier's power is > F
                if A[other] > F:
                    # Josh survives if his total damage is <= D - F
                    # D must be >= total_damage + F
                    D = total_damage + F
                    if D < min_D:
                        min_D = D
                        best_P = P
        
        if min_D != float('inf'):
            results.append("possible")
            results.append(f"{best_P} {min_D}")
        else:
            results.append("impossible")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()