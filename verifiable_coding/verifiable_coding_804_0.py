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
        
        # Try all possible P positions
        for P in range(1, N + 1):
            # Create the circular array with Josh at position P
            # The order is 1, 2, ..., P-1, N, P, P+1, ..., N-1
            # So the array is [A[0], A[1], ..., A[P-2], A[N-1], A[P-1], A[P], ..., A[N-2]]
            # But since P is 1-based, we need to adjust indices
            # For P=1, the array is [A[0], A[1], ..., A[N-2], A[N-1]]
            # For P=2, the array is [A[0], A[1], ..., A[N-2], A[N-1], A[0]]
            # So the array is [A[0], A[1], ..., A[P-2], A[N-1], A[0], A[1], ..., A[P-1]]
            # But since we are using 0-based indices, we need to adjust accordingly
            # Create the array in order
            arr = []
            for i in range(N):
                if i < P - 1:
                    arr.append(A[i])
                elif i == P - 1:
                    arr.append(0)  # Josh's position, represented as 0
                else:
                    arr.append(A[i - 1])
            
            # Now simulate the process
            # We need to find the order of attacks and calculate the total damage to Josh
            # The attack order is determined by the circular arrangement
            # The initial attacker is soldier 1 (index 0)
            # We need to simulate the process until there are two soldiers left
            # Then, we check if Josh can survive the Chefland attack
            
            # Simulate the attack process
            # We'll use a list to represent the current soldiers
            soldiers = arr.copy()
            current_attacker = 0  # index of the current attacker
            D = 0  # total damage to Josh
            while len(soldiers) > 2:
                # The attacker attacks the next soldier to the right
                next_attacker = (current_attacker + 1) % len(soldiers)
                if next_attacker == 0:
                    # The attacker is Josh, he doesn't attack
                    # So the next attacker is the one to the right of Josh
                    next_attacker = (current_attacker + 2) % len(soldiers)
                # The attacker attacks the next soldier
                attacked = next_attacker
                if attacked == 0:
                    # Josh is attacked
                    D += soldiers[attacked]
                    if D > F:
                        break
                else:
                    # Another soldier is attacked, he dies
                    soldiers.pop(attacked)
                # The next attacker is the soldier to the right of the current attacker
                current_attacker = next_attacker
            
            # Now, there are two soldiers left
            # Check if both are Josh and another soldier
            if len(soldiers) == 2:
                # Check if Josh is one of them
                if soldiers[0] == 0 or soldiers[1] == 0:
                    # Check if the other soldier's sword is > F
                    other = soldiers[1] if soldiers[0] == 0 else soldiers[0]
                    if other > F:
                        # Josh survives if D >= F
                        if D >= F:
                            possible = True
                            if D < min_D:
                                min_D = D
                                best_P = P
        
        if possible:
            results.append("possible")
            results.append(f"{best_P} {min_D}")
        else:
            results.append("impossible")
    
    for line in results:
        print(line)

if __name__ == '__main__':
    solve()