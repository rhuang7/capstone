import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        S = data[i].decode()
        total = 0
        min_char = min(S)
        max_char = max(S)
        
        # Calculate the total points if all characters are changed to min_char
        total_min = sum(ord(c) - ord(min_char) for c in S)
        
        # Calculate the total points if all characters are changed to max_char
        total_max = sum(ord(max_char) - ord(c) for c in S)
        
        # The answer is the absolute value of the minimum of total_min and total_max
        results.append(str(min(abs(total_min), abs(total_max))))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()