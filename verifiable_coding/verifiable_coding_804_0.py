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
        min_D = float('inf')
        best_P = -1
        
        # Try all possible P positions
        for P in range(1, N + 1):
            # Create the circular array with Josh's position as D
            # The array is [A[0], A[1], ..., A[N-2], D]
            # The order is 1, 2, ..., P-1, N, P, P+1, ..., N-1
            # So the array is [A[0], A[1], ..., A[P-2], D, A[P-1], ..., A[N-2]]
            # We need to compute the total damage Josh will take before Chefland's attack
            # This is the sum of all the attack powers that hit Josh before there are two soldiers left
            
            # The soldiers are in the order: 1, 2, ..., P-1, N, P, P+1, ..., N-1
            # So the array is [A[0], A[1], ..., A[P-2], D, A[P-1], ..., A[N-2]]
            # We need to simulate the process of elimination until two soldiers are left
            
            # We can simulate the process using a list to represent the current soldiers
            soldiers = []
            for i in range(N - 1):
                soldiers.append(A[i])
            soldiers.append(0)  # D is the power of Josh
            
            # The initial attacking soldier is 1 (index 0)
            current = 0
            D = 0
            while len(soldiers) > 2:
                # The attacking soldier is current
                # The next soldier is (current + 1) % len(soldiers)
                next_soldier = (current + 1) % len(soldiers)
                # The next soldier is killed
                soldiers.pop(next_soldier)
                # The new attacking soldier is next_soldier (if it exists)
                # But since we removed the next_soldier, the new current is next_soldier - 1 if next_soldier > current
                # Or next_soldier if next_soldier < current
                # So current = next_soldier if next_soldier < current else next_soldier - 1
                if next_soldier > current:
                    current = next_soldier - 1
                else:
                    current = next_soldier
            
            # Now, there are two soldiers left: Josh and one other
            # We need to check if both survive Chefland's attack
            # Josh survives if D >= F
            # The other soldier survives if his power > F
            
            # The two soldiers are at positions current and (current + 1) % len(soldiers)
            # But since we have two soldiers, we can check their powers
            # The first soldier is at index 0, the second at index 1
            # But we need to check which one is Josh
            # Josh is the one with power D
            # So we need to find which of the two is Josh
            
            # The soldiers list has two elements: one is D, the other is A[i]
            # We need to find the index of D
            if soldiers[0] == 0:
                josh_idx = 0
            else:
                josh_idx = 1
            
            # Check if both survive
            if soldiers[josh_idx] >= F and soldiers[1 - josh_idx] > F:
                # Josh survives
                D = soldiers[josh_idx] + soldiers[1 - josh_idx] - F
                if D < min_D:
                    min_D = D
                    best_P = P
        
        if best_P == -1:
            results.append("impossible")
        else:
            results.append("possible")
            results.append(f"{best_P} {min_D}")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()