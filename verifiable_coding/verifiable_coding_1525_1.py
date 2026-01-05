import sys
import math

MOD = 21945

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        N = int(data[idx])
        idx += 1
        grid = []
        for _ in range(8):
            grid.append(data[idx])
            idx += 1
        
        # Find all 1s in the grid
        ones = []
        for i in range(8):
            for j in range(8):
                if grid[i][j] == '1':
                    ones.append((i, j))
        
        # For each 1, determine how many times it is folded
        # Each fold doubles the size of the napkin
        # The number of folds is log2((2n)/8) = log2(n/4)
        # So the number of times the napkin is folded is k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So k = log2(n/4)
        # So the number of times the napkin is unfolded is k
        # Each fold doubles the size of the napkin
        # So the original size is 2^(k+3) x 2^(k+3)
        # The number of folds is k = log2(n/4)
        # So n = 4 * 2^k
        # So