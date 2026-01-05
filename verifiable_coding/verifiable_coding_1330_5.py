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
        A = int(data[idx])
        B = int(data[idx+1])
        idx += 2
        c = list(map(int, data[idx:idx+A*B]))
        idx += A*B
        d = list(map(int, data[idx:idx+A*B]))
        idx += A*B
        votes = []
        for i in range(A*B):
            votes.append((c[i], d[i]))
        # Sort the districts based on the maximum of c[i] and d[i]
        # We want to prioritize districts where P1's vote is higher
        # So we sort by the maximum of c[i] and d[i], and then by c[i] in descending order
        votes.sort(key=lambda x: (-max(x[0], x[1]), -x[0]))
        # Now, we need to group them into A states, each with B districts
        # For each state, we need to find the maximum value in the 2B values
        # and determine which party wins
        count_p1 = 0
        for i in range(0, A*B, B):
            state = votes[i:i+B]
            max_val = -1
            max_party = ''
            for (c_val, d_val) in state:
                if max_val < max(c_val, d_val):
                    max_val = max(c_val, d_val)
                    if c_val == max_val:
                        max_party = 'P1'
                    else:
                        max_party = 'P2'
            if max_party == 'P1':
                count_p1 += 1
        results.append(str(count_p1))
    print('\n'.join(results))

if __name__ == '__main__':
    solve()