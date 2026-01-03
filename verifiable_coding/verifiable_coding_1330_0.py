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
        
        # Create a list of tuples (c_i, d_i) for each district
        districts = list(zip(c, d))
        
        # For each district, create a list of (value, is_c) where value is the vote and is_c indicates if it's P1's vote
        # We sort this list in descending order to prioritize the highest values
        sorted_districts = sorted([(val, is_c) for val, is_c in [(c[i], True) for i in range(A*B)] + [(d[i], False) for i in range(A*B)]], reverse=True)
        
        # We need to select B districts for each state, and for each state, the maximum value determines the winner
        # We want to maximize the number of states where P1 wins, i.e., the maximum value in the state is from P1
        # So, we try to select B districts such that the maximum value is from P1
        # We can do this greedily: for each state, select the top B districts, and check if the maximum is from P1
        # We need to do this for A states
        
        count_p1 = 0
        remaining = A*B
        for _ in range(A):
            # Select B districts
            state = sorted_districts[:B]
            # Find the maximum value in the state
            max_val = max(state, key=lambda x: x[0])
            # Check if the maximum is from P1
            if max_val[1]:
                count_p1 += 1
            # Remove these B districts from the list
            sorted_districts = sorted_districts[B:]
        
        results.append(str(count_p1))
    
    print('\n'.join(results))

if __name__ == '__main__':
    solve()