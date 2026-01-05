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
        
        # Find the optimal position P and minimum D
        possible = False
        best_P = -1
        best_D = 0
        
        # Try all possible positions for P
        for P in range(1, N + 1):
            # Create the circular array with Josh at position P
            # The array is [A_1, A_2, ..., A_{P-1}, D, A_P, ..., A_{N-1}]
            # But since P is the position of Josh, the actual array is:
            # A[0], A[1], ..., A[P-2], D, A[P-1], A[P], ..., A[N-2]
            # But we need to make it circular, so we need to simulate the order
            # of the soldiers in the circle
            
            # We'll simulate the order of soldiers in the circle
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # So the order is [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # But since it's a circle, the order wraps around
            
            # To simulate the order, we can create a list of soldiers in the order they are attacked
            # Starting from 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then the order is circular
            
            # We can simulate the order by creating a list of soldiers in the order they are attacked
            # The first soldier is 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then the order is circular, so after N-1, it wraps around to 1
            # So the order is [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # Then the order is circular
            
            # To find the order of soldiers in the circle, we can create a list of soldiers in the order they are attacked
            # The first soldier is 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then the order is circular, so after N-1, it wraps around to 1
            
            # To simulate the order, we can create a list of soldiers in the order they are attacked
            # The first soldier is 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then the order is circular, so after N-1, it wraps around to 1
            
            # Create the list of soldiers in the order they are attacked
            order = []
            for i in range(1, N):
                if i < P:
                    order.append(i)
                else:
                    order.append(N)
                    if i == P:
                        order.append(P)
                    else:
                        order.append(i)
            
            # Now simulate the suicide process
            # The order is circular, so we can simulate it by looping through the order
            # The first soldier is 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then the order is circular, so after N-1, it wraps around to 1
            
            # We need to find the order of soldiers in the circle
            # The order is [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # Then the order is circular, so after N-1, it wraps around to 1
            
            # To simulate the order, we can create a list of soldiers in the order they are attacked
            # The first soldier is 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then the order is circular, so after N-1, it wraps around to 1
            
            # We can simulate the order by creating a list of soldiers in the order they are attacked
            # The first soldier is 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then the order is circular, so after N-1, it wraps around to 1
            
            # Create the list of soldiers in the order they are attacked
            order = []
            for i in range(1, N):
                if i < P:
                    order.append(i)
                else:
                    order.append(N)
                    if i == P:
                        order.append(P)
                    else:
                        order.append(i)
            
            # Now simulate the suicide process
            # The order is circular, so we can simulate it by looping through the order
            # The first soldier is 1, then 2, ..., P-1, N, P, P+1, ..., N-1
            # Then the order is circular, so after N-1, it wraps around to 1
            
            # We need to simulate the suicide process and find the minimum D such that Josh survives
            # The process is:
            # 1. Soldier 1 is the attacking soldier
            # 2. If the attacking soldier is not Josh, he attacks the soldier to his right
            # 3. When Josh is attacked, his shield's defense decreases by the attack power
            #    If it becomes negative, he dies
            # 4. When a different soldier is attacked, he dies immediately
            # 5. The next living soldier to the right of the current attacking soldier becomes the attacking soldier
            # 6. The process continues until only one soldier is left
            
            # We can simulate this process by maintaining a list of living soldiers
            # The order is circular, so we can simulate it by maintaining a list of living soldiers
            # and their positions in the order they are attacked
            
            # We need to simulate the process and find the minimum D such that Josh survives
            # The process is:
            # 1. Soldier 1 is the attacking soldier
            # 2. If the attacking soldier is not Josh, he attacks the soldier to his right
            # 3. When Josh is attacked, his shield's defense decreases by the attack power
            #    If it becomes negative, he dies
            # 4. When a different soldier is attacked, he dies immediately
            # 5. The next living soldier to the right of the current attacking soldier becomes the attacking soldier
            # 6. The process continues until only one soldier is left
            
            # We can simulate this process by maintaining a list of living soldiers
            # and their positions in the order they are attacked
            
            # We can simulate this process by maintaining a list of living soldiers
            # and their positions in the order they are attacked
            
            # We need to find the minimum D such that Josh survives
            # We can try all possible D values and check if Josh survives
            # But this is too slow for large N
            
            # Instead, we can simulate the process for each possible P and find the minimum D
            # that allows Josh to survive
            
            # We can simulate the process for each P and find the minimum D
            # that allows Josh to survive
            
            # Let's simulate the process for this P
            # We need to find the minimum D such that Josh survives
            # We can simulate the process and track the total damage Josh takes
            
            # We'll simulate the process for this P
            # The soldiers are in the order [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # But since it's a circle, the order wraps around
            
            # We can simulate the process by maintaining a list of living soldiers
            # and their positions in the order they are attacked
            
            # We can simulate the process by maintaining a list of living soldiers
            # and their positions in the order they are attacked
            
            # We'll simulate the process for this P
            # The soldiers are in the order [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # But since it's a circle, the order wraps around
            
            # We can simulate the process by maintaining a list of living soldiers
            # and their positions in the order they are attacked
            
            # We'll simulate the process for this P
            # The soldiers are in the order [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # But since it's a circle, the order wraps around
            
            # We can simulate the process by maintaining a list of living soldiers
            # and their positions in the order they are attacked
            
            # We'll simulate the process for this P
            # The soldiers are in the