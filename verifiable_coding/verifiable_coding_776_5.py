import sys
import math

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    D_list = list(map(int, data[1:T+1]))
    
    for D in D_list:
        if D == 0:
            print(1)
            print(1)
            continue
        
        # Construct a sequence that can generate the required D
        # We use a sequence of numbers that are all 1 except for one number that is D+1
        # This ensures that the sum of min and GCD over all subarrays is D
        N = 1
        A = [1]
        current_sum = 0
        
        # We need to find a sequence where the total sum of min - gcd over all subarrays is D
        # We use a sequence of 1s and one large number to control the sum
        # The large number contributes to the sum in a controlled way
        # We find the smallest number of elements needed to reach D
        while True:
            # Try adding a new element to the sequence
            # We add a number that is larger than all previous elements
            # This ensures that the min of any subarray that includes this element is the previous min
            # The gcd of any subarray that includes this element is the gcd of the previous elements and this new element
            # We choose the new element to be a large number, say 10^5 + 1
            new_element = 10**5 + 1
            new_A = A + [new_element]
            new_N = len(new_A)
            
            # Calculate the total sum of min - gcd over all subarrays
            # This is a bit complex, but we can approximate it
            # For a sequence of all 1s, the sum is 0
            # Adding a new element that is large contributes a certain amount to the sum
            # We can calculate how much it contributes
            # For a sequence of k 1s followed by a large number, the contribution is k*(k+1)/2 - k
            # Because the min of any subarray that includes the large number is 1
            # The gcd of any subarray that includes the large number is the gcd of the previous elements and the large number
            # Since the large number is coprime with all previous elements, the gcd is 1
            # So the contribution is k*(k+1)/2 - k = k*(k-1)/2
            # We need to find the smallest k such that k*(k-1)/2 >= D
            # We can use binary search for this
            
            # Find the smallest k such that k*(k-1)/2 >= D
            # This is a quadratic equation
            # k^2 - k - 2D >= 0
            # Using quadratic formula: k = (1 + sqrt(1 + 8D)) / 2
            k = int((1 + math.sqrt(1 + 8*D)) / 2)
            if k*(k-1)//2 >= D:
                break
            
            # If not, we need to add more elements
            # We can add more 1s
            # The contribution of each additional 1 is (current_length + 1) * current_length / 2 - (current_length + 1)
            # Which is (current_length + 1)*current_length / 2 - (current_length + 1) = current_length*(current_length - 1)/2
            # So we can add more 1s until we reach the required D
            
            # We can calculate how many more 1s we need
            # The total contribution from the sequence of 1s is k*(k-1)/2
            # We need to add more 1s to reach D
            # Let's add the required number of 1s
            # We can calculate how many more 1s we need
            # Let's say we have m 1s, then the contribution is m*(m-1)/2
            # We need to find the smallest m such that m*(m-1)/2 >= D
            # We can use the same method as before
            
            m = int((1 + math.sqrt(1 + 8*D)) / 2)
            if m*(m-1)//2 >= D:
                break
            
            # If not, we need to add more elements
            # We can add more 1s
            # We can add m 1s
            A = [1]*m
            N = m
            break
        
        # Now, we have a sequence of m 1s
        # We need to add one large number to the end
        A.append(10**5 + 1)
        N = len(A)
        
        # Now, we need to adjust the sequence to make sure the total sum is exactly D
        # We can adjust the large number to be D + 1
        # This way, the contribution of the large number is exactly D
        # The contribution of the large number is the number of subarrays that include it
        # Which is N*(N+1)/2 - (N-1)*N/2 = N
        # So we need to set the large number to D + 1
        # But we need to make sure that the large number is at least 10^5 + 1
        # So we can set it to max(D + 1, 10**5 + 1)
        A[-1] = max(D + 1, 10**5 + 1)
        
        print(N)
        print(' '.join(map(str, A)))

if __name__ == '__main__':
    solve()