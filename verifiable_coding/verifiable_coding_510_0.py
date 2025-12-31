import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    S = data[idx]
    idx += 1
    Q = int(data[idx])
    idx += 1
    
    S = list(S)
    
    for _ in range(Q):
        query_type = int(data[idx])
        idx += 1
        if query_type == 1:
            i_q = int(data[idx]) - 1
            idx += 1
            c_q = data[idx]
            idx += 1
            if S[i_q] != c_q:
                S[i_q] = c_q
        else:
            l_q = int(data[idx]) - 1
            idx += 1
            r_q = int(data[idx]) - 1
            idx += 1
            unique_chars = set()
            for i in range(l_q, r_q + 1):
                unique_chars.add(S[i])
            print(len(unique_chars))
            
if __name__ == '__main__':
    solve()