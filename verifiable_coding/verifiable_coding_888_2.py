import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    S = data[0]
    T = data[1]
    Q = int(data[2])
    queries = list(map(int, data[3:3+Q]))
    
    len_S = len(S)
    len_T = len(T)
    
    # Precompute the pattern for T in S
    pattern = []
    for i in range(len_S):
        pattern.append(S[i])
    
    # Precompute the occurrences of T in a row of the pyramid
    # For a row N, the row has N characters
    # The characters are S[0], S[0], S[0], ... (cyclic)
    # So the row is S[0] * N
    
    # But we need to find the number of occurrences of T in this row
    # So we need to find how many times T appears as a substring in a string of N characters, all being S[0]
    
    # If T is longer than N, answer is 0
    # If T is shorter or equal to N, we need to find how many times T appears in a string of N S[0]s
    
    # Precompute the number of occurrences of T in a string of length L made of S[0]
    # We can do this by checking if T is made of S[0]s
    # If T is made of S[0]s, then the number of occurrences is (L - len_T + 1)
    # Else, it's 0
    
    # Check if T is made of S[0]s
    is_all_same = True
    for c in T:
        if c != S[0]:
            is_all_same = False
            break
    
    # Precompute the number of occurrences for any L
    def count_occurrences(L):
        if len_T > L:
            return 0
        if not is_all_same:
            return 0
        return L - len_T + 1
    
    # Process queries
    for N in queries:
        L = N
        print(count_occurrences(L))
        
if __name__ == '__main__':
    solve()