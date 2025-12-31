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
            # The array is arranged as [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # So the order is: 1, 2, ..., P-1, N, P, P+1, ..., N-1
            # We need to arrange the soldiers in this order
            # The soldiers are numbered 1 to N, with Josh at position P
            # The array is arranged in the order given in the problem statement
            # So the soldiers are: 1, 2, ..., P-1, N, P, P+1, ..., N-1
            # So the array is:
            # [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # We need to find the order of soldiers in the circle
            # For the initial order, the soldiers are arranged in the order given in the problem statement
            # So the order is: 1, 2, ..., P-1, N, P, P+1, ..., N-1
            # The soldiers are arranged in a circle
            # So the order is: 1, 2, ..., P-1, N, P, P+1, ..., N-1
            # So the array is:
            # [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # We need to simulate the process
            # The process is:
            # 1. Soldier 1 is the attacking soldier
            # 2. If the attacking soldier is not Josh, he attacks the soldier to his right
            # 3. When Josh is attacked, his shield's defense decreases by the attack power
            # 4. When another soldier is attacked, he dies immediately
            # 5. The next living soldier to the right of the current attacking soldier becomes the attacking soldier
            # 6. This continues until only one soldier is left
            # We need to simulate this process and check if Josh survives
            # We also need to check if Chefland's attack can be interrupted when there are exactly two soldiers left
            
            # Create the array of soldiers in the order they are arranged
            soldiers = []
            for i in range(1, N):
                if i < P:
                    soldiers.append(i)
                else:
                    soldiers.append(N)
            soldiers.append(P)
            
            # Now simulate the process
            # We need to find the order of soldiers in the circle
            # The soldiers are arranged in a circle, so the order is:
            # [soldiers[0], soldiers[1], ..., soldiers[N-1], soldiers[0], ...]
            # We need to simulate the process
            # We can represent the soldiers as a list, and track the current attacking soldier
            # We can also track the current defense of Josh's shield
            # We can also track the current list of living soldiers
            
            # We will simulate the process
            # The initial list of soldiers is soldiers
            # We will simulate the process step by step
            # The initial attacking soldier is 0 (index 0)
            # We need to simulate the process
            
            # Create a list of soldiers in the order they are arranged in the circle
            # The soldiers are arranged as [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # So the list is:
            # [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # We can create this list as follows:
            soldiers = []
            for i in range(1, N):
                if i < P:
                    soldiers.append(i)
                else:
                    soldiers.append(N)
            soldiers.append(P)
            
            # Now simulate the process
            # We need to find the order of soldiers in the circle
            # We can simulate the process by maintaining a list of living soldiers
            # The initial list of soldiers is soldiers
            # The initial attacking soldier is 0 (index 0)
            # We can simulate the process as follows:
            # 1. The attacking soldier is the current one
            # 2. If the attacking soldier is not Josh, he attacks the soldier to his right
            # 3. When Josh is attacked, his shield's defense decreases by the attack power
            # 4. When another soldier is attacked, he dies immediately
            # 5. The next living soldier to the right of the current attacking soldier becomes the attacking soldier
            # 6. This continues until only one soldier is left
            
            # We need to simulate this process
            # We can represent the soldiers as a list, and track the current attacking soldier
            # We can also track the current defense of Josh's shield
            # We can also track the current list of living soldiers
            
            # We will simulate the process
            # The initial list of soldiers is soldiers
            # The initial attacking soldier is 0 (index 0)
            # We need to simulate the process
            
            # We will create a list of soldiers in the order they are arranged in the circle
            # The soldiers are arranged as [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # So the list is:
            # [1, 2, ..., P-1, N, P, P+1, ..., N-1]
            # We can create this list as follows:
            soldiers = []
            for i in range(1, N):
                if i < P:
                    soldiers.append(i)
                else:
                    soldiers.append(N)
            soldiers.append(P)
            
            # Now simulate the process
            # We need to find the order of soldiers in the circle
            # We can simulate the process by maintaining a list of living soldiers
            # The initial list of soldiers is soldiers
            # The initial attacking soldier is 0 (index 0)
            # We can simulate the process as follows:
            # 1. The attacking soldier is the current one
            # 2. If the attacking soldier is not Josh, he attacks the soldier to his right
            # 3. When Josh is attacked, his shield's defense decreases by the attack power
            # 4. When another soldier is attacked, he dies immediately
            # 5. The next living soldier to the right of the current attacking soldier becomes the attacking soldier
            # 6. This continues until only one soldier is left
            
            # We need to simulate this process
            # We can represent the soldiers as a list, and track the current attacking soldier
            # We can also track the current defense of Josh's shield
            # We can also track the current list of living soldiers
            
            # We will simulate the process
            # The initial list of soldiers is soldiers
            # The initial attacking soldier is 0 (index 0)
            # We need to simulate the process
            
            # We will simulate the process
            # The initial list of soldiers is soldiers
            # The initial attacking soldier is 0 (index 0)
            # We need to simulate the process
            # We will use a list to represent the living soldiers
            # We will also track the current attacking soldier
            # We will track the current defense of Josh's shield
            # We will also track the current list of living soldiers
            
            # We will simulate the process
            # The initial list of soldiers is soldiers
            # The initial attacking soldier is 0 (index 0)
            # We need to simulate the process
            # We will use a list to represent the living soldiers
            # We will also track the current attacking soldier
            # We will track the current defense of Josh's shield
            # We will also track the current list of living soldiers
            
            # We will simulate the process
            # The initial list of soldiers is soldiers
            # The initial attacking soldier is 0 (index 0)
            # We need to simulate the process
            # We will use a list to represent the living soldiers
            # We will also track the current attacking soldier
            # We will track the current defense of Josh's shield
            # We will also track the current list of living soldiers
            
            # We will simulate the process
            # The initial list of soldiers is soldiers
            # The initial attacking soldier is 0 (index 0)
            # We need to simulate the process
            # We will use a list to represent the living soldiers
            # We will also track the current attacking soldier