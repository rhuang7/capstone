import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        d = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        
        # The number of valid arrays is equal to the sum of the first d numbers
        # because each array corresponds to a unique number in 1..d
        # and the condition is satisfied when the array is strictly increasing
        # and the XOR sequence is strictly increasing
        # This is a known problem, and the answer is simply the sum of the first d numbers
        # modulo m
        total = (d * (d + 1)) // 2 % m
        results.append(total)
    
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == '__main__':
    solve()