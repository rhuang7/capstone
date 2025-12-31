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
        arr = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Sort the array
        arr.sort()
        
        # Maximum area is product of two largest numbers
        max_area = arr[-1] * arr[-2]
        
        # Minimum area is product of two smallest numbers
        min_area = arr[0] * arr[1]
        
        results.append(f"{max_area} {min_area}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()