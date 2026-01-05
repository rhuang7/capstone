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
        N = int(data[idx])
        K = int(data[idx+1])
        idx += 2
        
        forgotten = data[idx:idx+N]
        idx += N
        
        modern_words = set()
        
        for _ in range(K):
            L = int(data[idx])
            idx += 1
            for _ in range(L):
                modern_words.add(data[idx])
                idx += 1
        
        output = []
        for word in forgotten:
            if word in modern_words:
                output.append("YES")
            else:
                output.append("NO")
        
        results.append(" ".join(output))
    
    print("\n".join(results))

if __name__ == '__main__':
    solve()