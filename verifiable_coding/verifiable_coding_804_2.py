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
        
        # Find the optimal P and D
        possible = False
        min_D = float('inf')
        best_P = -1
        
        # Try all possible positions for Josh (P)
        for P in range(1, N + 1):
            # Create the circular array with Josh's position as D
            # The order is 1, 2, ..., P-1, N, P, P+1, ..., N-1
            # So the array is [A[0], A[1], ..., A[P-2], A[N-1], D, A[N-2], ..., A[P-1]]
            # We need to make sure that the order is correct
            # We can create the array as follows:
            arr = []
            for i in range(N):
                if i < P - 1:
                    arr.append(A[i])
                elif i == P - 1:
                    arr.append(A[N-1])
                else:
                    arr.append(A[i-1])
            # Now, simulate the suicide process
            # We need to find the order of attacks and calculate the total damage to Josh
            # We can simulate the process with a list of alive soldiers
            alive = [i for i in range(N)]
            current = 0  # starting with soldier 1 (index 0)
            D_total = 0
            while len(alive) > 2:
                # The attacker is current
                attacker = alive[current]
                # The next soldier to the right is (current + 1) % len(alive)
                next_soldier = (current + 1) % len(alive)
                # The attacker attacks the next soldier
                # If the next soldier is Josh, he defends
                if next_soldier == P - 1:  # Josh is at position P (0-based index P-1)
                    # Josh defends, so D_total += A[next_soldier]
                    D_total += arr[next_soldier]
                else:
                    # The next soldier dies
                    alive.pop(next_soldier)
                # The next attacker is the soldier to the right of the current attacker
                current = (current + 1) % len(alive)
            
            # Now, there are exactly two soldiers left
            # The two soldiers are Josh and another one
            # We need to check if both survive Chefland's attack
            # The other soldier must have A > F
            # Josh must have D_total >= F
            # So, check if the other soldier's A is > F
            # The other soldier is the one not equal to P-1
            other = [i for i in alive if i != P - 1][0]
            if arr[other] > F and D_total >= F:
                possible = True
                if D_total < min_D:
                    min_D = D_total
                    best_P = P
        
        if possible:
            results.append("possible")
            results.append(f"{best_P} {min_D}")
        else:
            results.append("impossible")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()