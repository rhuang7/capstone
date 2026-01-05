import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    results = []
    
    for _ in range(T):
        N = int(data[index])
        L = int(data[index+1])
        R = int(data[index+2])
        index += 3
        
        # Minimum sum: all elements are 1
        min_sum = N * 1
        
        # Maximum sum: use the largest possible numbers that satisfy the conditions
        # The largest possible numbers are 1, 2, 4, 8, ..., 2^k
        # We need to select numbers such that each number is even and half is present
        # So the maximum sum is achieved by using the largest possible numbers that satisfy the condition
        # The maximum number of unique elements is R, so we take the first R numbers in the sequence 1, 2, 4, 8, ...
        # But since each even number must have its half present, the sequence is 1, 2, 4, 8, ...
        # So the maximum sum is the sum of the first R numbers in this sequence, but with each number appearing once
        # However, since the array has N elements, we need to repeat the largest numbers as needed
        # So the maximum sum is the sum of the first R numbers in the sequence, and then fill the rest with the largest number
        max_sum = 0
        unique_numbers = []
        current = 1
        while len(unique_numbers) < R:
            unique_numbers.append(current)
            current *= 2
        
        # Sum of the first R numbers
        max_sum = sum(unique_numbers)
        
        # Fill the rest of the array with the largest number
        max_sum += (N - R) * unique_numbers[-1]
        
        results.append(f"{min_sum} {max_sum}")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()