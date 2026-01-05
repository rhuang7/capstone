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
        N, K = int(data[idx]), int(data[idx+1])
        idx += 2
        A = list(map(int, data[idx:idx+N]))
        idx += N
        l = []
        r = []
        for _ in range(N):
            li = int(data[idx])
            ri = int(data[idx+1])
            l.append(li)
            r.append(ri)
            idx += 2
        # Compute A^1
        curr = A
        # For K=1, output is A
        if K == 1:
            results.append(' '.join(map(str, curr)))
            continue
        # For K > 1, compute using binary exponentiation
        # We'll use a binary exponentiation approach for the sequence operation
        # Since K can be up to 5e7, we need an efficient way
        # We'll represent the sequence operations as matrices or use fast exponentiation
        # However, due to the nature of XOR and the sequence operation, we can find a pattern
        # Let's use binary exponentiation on the sequence operation
        # We'll represent the sequence operation as a function
        def apply_operation(seq):
            new_seq = [0] * N
            for i in range(N):
                l_i = l[i] - 1
                r_i = r[i] - 1
                # Compute XOR of subarray from l_i to r_i
                xor_val = 0
                for j in range(l_i, r_i + 1):
                    xor_val ^= seq[j]
                new_seq[i] = xor_val
            return new_seq
        # Binary exponentiation
        def power_operation(op, power):
            result = [0] * N
            # Initialize result as identity operation (no change)
            for i in range(N):
                result[i] = 0
            while power > 0:
                if power % 2 == 1:
                    result = apply_operation(result)
                op = apply_operation(op)
                power //= 2
            return result
        # Compute A^K
        power = K
        result_seq = power_operation(curr, power)
        results.append(' '.join(map(str, result_seq)))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()