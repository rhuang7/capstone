import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    
    results = []
    
    for case in range(1, T + 1):
        L = int(data[index])
        K = int(data[index + 1])
        index += 2
        
        if K == 0:
            results.append(f"Case {case}: 0")
            continue
        
        if K > L:
            results.append(f"Case {case}: 0")
            continue
        
        count = 0
        
        for i in range(1, L - K + 2):
            for j in range(1, L - K + 2):
                if i + j <= L - K + 1:
                    count += 1
        
        results.append(f"Case {case}: {count}")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()