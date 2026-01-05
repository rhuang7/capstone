import sys

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
        A = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Check if the array is a rainbow array
        is_rainbow = True
        # First part: 1 to 7
        count = 0
        for i in range(7):
            if i == 0:
                target = 1
            elif i == 6:
                target = 7
            else:
                target = i + 1
            while count < N and A[count] == target:
                count += 1
            if count == N:
                is_rainbow = False
                break
        if not is_rainbow:
            results.append("no")
            continue
        
        # Second part: 6 to 1
        count = 0
        for i in range(6, 0, -1):
            while count < N and A[count] == i:
                count += 1
            if count == N:
                is_rainbow = False
                break
        if is_rainbow:
            results.append("yes")
        else:
            results.append("no")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()