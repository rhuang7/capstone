import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        S = data[i].strip()
        if not S:
            results.append(0)
            continue
        
        # Calculate the total points for changing all characters to 'a'
        total = 0
        for c in S:
            total += ord(c) - ord('a')
        
        # Calculate the total points for changing all characters to 'z'
        total_z = 0
        for c in S:
            total_z += ord('z') - ord(c)
        
        # The minimum absolute value is the minimum of the two totals
        results.append(min(abs(total), abs(total_z)))
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()