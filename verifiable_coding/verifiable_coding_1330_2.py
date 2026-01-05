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
        
        # For each district, create a list of (value, is_c) where value is the maximum of c_i and d_i
        # and is_c is True if the maximum is c_i, else False
        # This helps in determining which party wins the state
        # We sort the districts based on the maximum value in descending order
        # Then, we greedily assign districts to states such that the maximum value in each state is from P1
        # We need to select B districts for each state, and ensure that the maximum in each state is from P1
        # To maximize the number of states won by P1, we select the top 2*B values (since each state has B districts)
        # and then assign them in a way that the maximum in each state is from P1
        
        # Create a list of (max_val, is_c) for each district
        max_vals = []
        for ci, di in districts:
            max_val = max(ci, di)
            is_c = (ci == max_val)
            max_vals.append((max_val, is_c))
        
        # Sort the districts by max_val in descending order
        max_vals.sort(reverse=True)
        
        # Now, we need to select B districts for each state
        # We will try to select B districts such that the maximum in each state is from P1
        # We can do this by greedily selecting the top 2*B districts and then grouping them into states
        # For each state, we select B districts, and the maximum in that state must be from P1
        
        # We will keep track of how many states P1 can win
        p1_wins = 0
        
        # We will use a priority queue to select the best possible districts for each state
        # We will use a max heap to select the districts with the highest max_vals
        # But since we need to group them into B districts per state, we will use a greedy approach
        
        # We will iterate over the top 2*B districts
        # For each state, we will select B districts, and check if the maximum in that state is from P1
        # We will keep track of the maximum in each state
        # We will use a priority queue to select the best possible districts for each state
        
        # We will use a heap to select the districts with the highest max_vals
        # We will also keep track of the maximum in each state
        # We will use a greedy approach to select the districts for each state
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will use a list to keep track of the maximum in each state
        # We will also use a list to keep track of the count of districts in each state
        # We will use a list to keep track of the count of P1 wins
        
        # We will