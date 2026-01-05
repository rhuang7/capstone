import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(T):
        X1 = int(data[index])
        X2 = int(data[index+1])
        X3 = int(data[index+2])
        V1 = int(data[index+3])
        V2 = int(data[index+4])
        index += 5
        
        # Calculate time for Chef and Kefa
        time_chef = (X3 - X1) / V1
        time_kefa = (X2 - X3) / V2
        
        if time_chef < time_kefa:
            results.append("Chef")
        elif time_chef > time_kefa:
            results.append("Kefa")
        else:
            results.append("Draw")
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()