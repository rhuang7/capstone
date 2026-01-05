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
        B = list(map(int, data[idx:idx+N]))
        idx += N
        
        # Calculate Alice's best possible sum
        alice_sum = sum(A)
        alice_sum -= min(A)
        
        # Calculate Bob's best possible sum
        bob_sum = sum(B)
        bob_sum -= min(B)
        
        if alice_sum < bob_sum:
            results.append("Alice")
        elif alice_sum > bob_sum:
            results.append("Bob")
        else:
            results.append("Draw")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()