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
        dish1 = data[index:index+4]
        index += 4
        dish2 = data[index:index+4]
        index += 4
        
        common = set(dish1) & set(dish2)
        if len(common) >= 2:
            results.append("similar")
        else:
            results.append("dissimilar")
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()