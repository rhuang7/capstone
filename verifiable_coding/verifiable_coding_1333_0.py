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
            results.append(1)
            continue
        # Check if B is valid
        valid = True
        for i in range(N):
            if i == 0:
                if B[i] != 0:
                    valid = False
                    break
            else:
                if B[i] < B[i-1]:
                    valid = False
                    break
        if not valid:
            results.append(0)
            continue
        # Compute the number of possible sequences A
        # B[i] = B[i-1] | A[i]
        # So A[i] must be such that B[i-1] | A[i] = B[i]
        # Also, A[i] must be <= B[i]
        # And A[i] must not have any bits set that are not in B[i]
        # So for each i, the number of possible A[i] is (number of bits set in B[i] - number of bits set in B[i-1]) + 1
        # But we need to make sure that B[i] is the OR of all previous A's
        # So we need to track the current OR value
        current_or = 0
        ans = 1
        for i in range(N):
            if i == 0:
                if B[i] != 0:
                    ans = 0
                    break
            else:
                if B[i] < B[i-1]:
                    ans = 0
                    break
                # The number of possible A[i] is the number of bits that are set in B[i] but not in B[i-1]
                # Because A[i] must be such that B[i-1] | A[i] = B[i]
                # So A[i] must have exactly the bits that are set in B[i] but not in B[i-1]
                # And the rest of the bits can be anything as long as they are already in B[i-1]
                # So the number of possible A[i] is 2^(number of bits that are set in B[i] but not in B[i-1])
                # But we need to make sure that A[i] is <= B[i]
                # So the number of possible A[i] is 2^(number of bits that are set in B[i] but not in B[i-1])
                # But we also need to make sure that B[i] is the OR of all previous A's
                # So we need to check if B[i] is the OR of all previous A's
                # Which is already ensured by the fact that B[i] >= B[i-1]
                # So we can proceed
                diff = B[i] ^ B[i-1]
                count = 0
                while diff:
                    if diff & 1:
                        count += 1
                    diff >>= 1
                ans = (ans * (1 << count)) % MOD
                current_or = B[i]
        results.append(ans)
    for res in results:
        print(res)

if __name__ == '__main__':
    solve()