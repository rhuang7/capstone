import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n, d = int(data[idx]), int(data[idx+1])
        idx += 2
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        # Calculate how much we can move from each pile to pile 1
        max_haybales = a[0]
        remaining_days = d
        
        for i in range(1, n):
            # Calculate the distance from pile i to pile 1
            distance = i
            # How many haybales can be moved from pile i to pile 1 in remaining_days
            move = min(a[i], remaining_days // distance)
            max_haybales += move
            remaining_days -= move * distance
        
        results.append(str(max_haybales))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()