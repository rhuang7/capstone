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
        alice_total = sum(A)
        alice_total -= min(A)
        
        # Calculate Bob's best possible sum
        bob_total = sum(B)
        bob_total -= min(B)
        
        if alice_total < bob_total:
            results.append("Alice")
        elif alice_total > bob_total:
            results.append("Bob")
        else:
            results.append("Draw")
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()