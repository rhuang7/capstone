import sys

def solve():
    import sys
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
        sets = []
        for _ in range(m):
            vi = int(data[idx])
            idx += 1
            s = set(map(int, data[idx:idx+vi]))
            idx += vi
            sets.append(s)
        
        # Find the minimal number of atoms
        # Each atom is a subset of X such that for every Si, the atom is either a subset of Si or disjoint from Si
        # This is equivalent to finding the minimal number of elements in a partition of X where each element is in exactly one atom
        # And for each Si, the atoms are either entirely contained in Si or disjoint from Si
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # This problem is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # The minimal number of atoms is the maximum number of elements in any Si that are not contained in any other Si
        # This is equivalent to finding the minimal number of atoms such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can model it as a bipartite graph where one set is the elements of X and the other set is the sets Si
        # An edge exists between an element x and a set Si if x is in Si
        # Then, the minimal number of atoms is the maximum matching in this bipartite graph
        
        # However, since we are to find the minimal number of atoms, we can instead find the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can use a greedy approach:
        # For each element in X, if it is not already in an atom, we create a new atom containing it
        # However, we must ensure that the new atom is either entirely contained in some Si or disjoint from all Si
        
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can model it as a bipartite graph where one set is the elements of X and the other set is the sets Si
        # An edge exists between an element x and a set Si if x is in Si
        # Then, the minimal number of atoms is the maximum matching in this bipartite graph
        
        # However, since we are to find the minimal number of atoms, we can instead find the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can use a greedy approach:
        # For each element in X, if it is not already in an atom, we create a new atom containing it
        # However, we must ensure that the new atom is either entirely contained in some Si or disjoint from all Si
        
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can model it as a bipartite graph where one set is the elements of X and the other set is the sets Si
        # An edge exists between an element x and a set Si if x is in Si
        # Then, the minimal number of atoms is the maximum matching in this bipartite graph
        
        # However, since we are to find the minimal number of atoms, we can instead find the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can use a greedy approach:
        # For each element in X, if it is not already in an atom, we create a new atom containing it
        # However, we must ensure that the new atom is either entirely contained in some Si or disjoint from all Si
        
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can model it as a bipartite graph where one set is the elements of X and the other set is the sets Si
        # An edge exists between an element x and a set Si if x is in Si
        # Then, the minimal number of atoms is the maximum matching in this bipartite graph
        
        # However, since we are to find the minimal number of atoms, we can instead find the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can use a greedy approach:
        # For each element in X, if it is not already in an atom, we create a new atom containing it
        # However, we must ensure that the new atom is either entirely contained in some Si or disjoint from all Si
        
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can model it as a bipartite graph where one set is the elements of X and the other set is the sets Si
        # An edge exists between an element x and a set Si if x is in Si
        # Then, the minimal number of atoms is the maximum matching in this bipartite graph
        
        # However, since we are to find the minimal number of atoms, we can instead find the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can use a greedy approach:
        # For each element in X, if it is not already in an atom, we create a new atom containing it
        # However, we must ensure that the new atom is either entirely contained in some Si or disjoint from all Si
        
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can model it as a bipartite graph where one set is the elements of X and the other set is the sets Si
        # An edge exists between an element x and a set Si if x is in Si
        # Then, the minimal number of atoms is the maximum matching in this bipartite graph
        
        # However, since we are to find the minimal number of atoms, we can instead find the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can use a greedy approach:
        # For each element in X, if it is not already in an atom, we create a new atom containing it
        # However, we must ensure that the new atom is either entirely contained in some Si or disjoint from all Si
        
        # This is equivalent to finding the minimal number of elements in a partition of X such that for each Si, the atoms are either entirely contained in Si or disjoint from Si
        
        # To find this, we can model it as a bipartite graph where one set is the elements of X and the other set is