import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    results = []
    
    for _ in range(t):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2
        
        # The minimal value is (a ^ x) + (b ^ x)
        # Let's find the minimal value by considering each bit
        # We want to minimize (a ^ x) + (b ^ x)
        # Let's find the bit where a and b differ
        # For each bit position, if a and b differ, we can set x's bit to 0 to minimize the sum
        # If they are the same, we can set x's bit to 0 or 1, but it doesn't affect the sum
        # So the minimal value is (a ^ b) << 1
        
        min_val = (a ^ b) << 1
        results.append(str(min_val))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()