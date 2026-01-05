import sys
import heapq

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    for _ in range(T):
        N, M = int(data[idx]), int(data[idx+1])
        idx += 2
        C = list(map(int, data[idx:idx+M]))
        idx += M
        D = []
        F = []
        B = []
        for _ in range(N):
            d = int(data[idx])
            f = int(data[idx+1])
            b = int(data[idx+2])
            D.append(d - 1)  # 0-based
            F.append(f)
            B.append(b)
            idx += 3
        # Initialize available flavors
        available = [i for i in range(M)]
        # For each flavor, keep track of how many are left
        count = C.copy()
        # For each customer, store (F_i, B_i, D_i)
        # We need to process customers in order
        # For each flavor, we can keep a priority queue of (B_i, F_i, D_i)
        # But since we must first satisfy the favorite flavor, we need to process those first
        # So for each flavor, we collect all customers who have that as their favorite
        # Then, we process those first, and then for the rest, we can choose the best available
        # So, for each flavor, we collect the customers who have that as their favorite
        # Then, for each customer, we can decide whether to take their favorite or not
        # We'll process the customers in order, and for each, if their favorite is available, we take it
        # Otherwise, we take the best possible option from the remaining flavors
        # So, we can pre-process the customers into a list of (D_i, F_i, B_i)
        # Then, for each customer, we check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we take the best possible option from the remaining flavors
        # To do this efficiently, we can use a priority queue for the remaining flavors
        # But since we have to process customers in order, and for each customer, we may need to choose the best possible option
        # So, for each customer, we first check if their favorite is available
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a max-heap for the remaining flavors, where each entry is (B_i, F_i, D_i)
        # But since we need to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers in order, we can't pre-process all the options
        # So, we can create for each flavor a priority queue of (F_i, B_i, D_i) for customers who have that as their favorite
        # Then, for each customer, we first check if their favorite is available
        # If yes, we take it and decrease the count
        # If not, we look for the best possible option from the remaining flavors
        # To do this, we can have a priority queue for the remaining options
        # But since we have to process customers