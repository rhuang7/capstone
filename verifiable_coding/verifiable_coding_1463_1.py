import sys
import math
from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    T = int(data[0])
    cases = list(map(int, data[1:T+1]))
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.isqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def get_prime_factors(n):
        factors = []
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.append(n)
        return factors
    
    def get_prime_factors_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list(n):
        factors = []
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.append(n)
        return factors
    
    def get_prime_factors_set_list(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <= n:
            if n % i == 0:
                factors.add(i)
                while n % i == 0:
                    n //= i
            i += 1
        if n > 1:
            factors.add(n)
        return factors
    
    def get_prime_factors_list_set(n):
        factors = set()
        i = 2
        while i * i <=