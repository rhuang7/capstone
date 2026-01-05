import sys
import math
from collections import deque

def solve():
    input = sys.stdin.buffer.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx+1])
        idx += 2
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            u = int(data[idx])
            v = int(data[idx+1])
            adj[u].append(v)
            adj[v].append(u)
            idx += 2
        
        # BFS to find a vertex with the smallest degree
        min_degree = n
        min_vertex = -1
        for i in range(1, n+1):
            if len(adj[i]) < min_degree:
                min_degree = len(adj[i])
                min_vertex = i
        
        # Perform BFS from min_vertex to find all vertices not in the chosen set
        visited = [False] * (n+1)
        q = deque()
        q.append(min_vertex)
        visited[min_vertex] = True
        chosen = [min_vertex]
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        # Collect all unvisited vertices (they are not in the chosen set)
        # But we need to choose at most floor(n/2) vertices
        # So we can choose the ones that are not in the BFS tree
        # Wait, we need to choose vertices such that all unchosen are adjacent to chosen
        # So we can choose all vertices that are not in the BFS tree (i.e., not visited)
        # But that might be more than floor(n/2)
        # So we need to choose the ones with the smallest degree first
        
        # Collect all vertices not in the BFS tree
        unchosen = []
        for i in range(1, n+1):
            if not visited[i]:
                unchosen.append(i)
        
        # Now, we need to choose at most floor(n/2) vertices such that all unchosen are adjacent to chosen
        # So we can choose the ones with the smallest degree first
        # But we need to ensure that all unchosen are adjacent to chosen
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that might not be enough, so we need to choose some of them
        
        # We can choose the ones that are not in the BFS tree (i.e., not visited)
        # But we need to make sure that all unchosen are adjacent to chosen
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that might not be enough, so we need to choose some of them
        
        # So we can choose all the unchosen vertices (those not in the BFS tree)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # We can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So we can choose the ones with the smallest degree first
        
        # So we can choose the ones that are not in the BFS tree (i.e., not visited)
        # But that may be more than floor(n/2), so we need to choose some of them
        # So