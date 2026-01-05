import sys

def solve():
    import sys
    input = sys.stdin.buffer.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    
    special_friends = set()
    for _ in range(N):
        friend = int(data[idx])
        idx += 1
        special_friends.add(friend)
    
    posts = []
    for _ in range(M):
        f = int(data[idx])
        idx += 1
        p = int(data[idx])
        idx += 1
        s = data[idx]
        idx += 1
        posts.append((f, p, s))
    
    # Sort special friends' posts by popularity descending
    special_posts = []
    other_posts = []
    
    for f, p, s in posts:
        if f in special_friends:
            special_posts.append((p, s))
        else:
            other_posts.append((p, s))
    
    # Sort special posts by popularity descending
    special_posts.sort(reverse=True)
    # Sort other posts by popularity descending
    other_posts.sort(reverse=True)
    
    # Output the results
    for p, s in special_posts:
        print(s)
    for p, s in other_posts:
        print(s)

if __name__ == '__main__':
    solve()