import sys
MOD = 10**9 + 7

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        B = list(map(int, data[idx:idx+N]))
        idx += N
        
        if B[0] == 0:
            # The first element of B must be the first element of A
            # Since B_1 = A_1, and B_1 is 0, A_1 must be 0
            # But then B_1 = 0, which is possible only if A_1 = 0
            # So the only possible A is [0, ...]
            # But we need to check if the rest of B is valid
            valid = True
            for i in range(1, N):
                if B[i] != B[i-1] | B[i]:
                    valid = False
                    break
            if valid:
                # The number of possible sequences is 1
                results.append(1)
            else:
                results.append(0)
            continue
        
        # Check if B is valid
        valid = True
        for i in range(1, N):
            if B[i] != B[i-1] | B[i]:
                valid = False
                break
        if not valid:
            results.append(0)
            continue
        
        # Now calculate the number of possible sequences A
        # B_i = B_{i-1} | A_i
        # So A_i can be any value such that B_{i-1} | A_i = B_i
        # And A_i must be <= B_i
        # Also, A_i must be such that B_{i-1} | A_i = B_i
        # So A_i can be any value in [0, B_i] that when OR with B_{i-1} gives B_i
        # The number of such A_i is (B_i & (~B_{i-1})) + 1
        # But we need to make sure that B_i >= B_{i-1}
        # Which is already ensured by the valid check
        res = 1
        prev = 0
        for i in range(N):
            if i == 0:
                prev = B[i]
                continue
            # A_i can be any value such that B_{i-1} | A_i = B_i
            # So A_i can be any value in [0, B_i] that when OR with B_{i-1} gives B_i
            # The number of such A_i is (B_i & (~B_{i-1})) + 1
            # But we need to make sure that B_i >= B_{i-1}
            # Which is already ensured by the valid check
            # So the number of choices for A_i is (B_i & (~B_{i-1})) + 1
            # But we need to check if B_i is not equal to B_{i-1}
            # If B_i == B_{i-1}, then A_i must be equal to B_{i-1}
            # So the number of choices is 1
            if B[i] == prev:
                res = 0
                break
            # Calculate the number of possible A_i
            # A_i can be any value in [0, B_i] that when OR with prev gives B_i
            # So A_i must be such that (A_i & prev) == prev and (A_i | prev) == B_i
            # So A_i must be a subset of B_i's bits that are not in prev
            # The number of such A_i is (B_i & (~prev)) + 1
            # But since B_i is the OR of prev and A_i, and B_i >= prev
            # So the number of possible A_i is (B_i & (~prev)) + 1
            # But since B_i is fixed, and prev is fixed, we can calculate it
            count = (B[i] & (~prev)) + 1
            res = (res * count) % MOD
            prev = B[i]
        results.append(res)
    
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()