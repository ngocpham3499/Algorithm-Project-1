def minSwapsCouples(self, row: List[int]) -> int:
        
        def find(a):
            if parent[a] != a: # path compression
                parent[a] = find(parent[a]) # if parent[a] is not root, then find root of parent[a] | recursive call
            return parent[a] 
        
        def union(a, b):
            rootA = find(a) # find root of a
            rootB = find(b) # find root of b
            if rootA != rootB: # if a and b are not in the same set
                parent[rootA] = rootB # make root of a as parent of root of b

        n = len(row) // 2 # number of couples
        parent = [i for i in range(n)] # parent array to store root of each couple
        
        for i in range(0, len(row), 2): # iterate over couples | 2 step
            union(row[i] //2, row[i+1] //2) # union of couples | //2 to get couple number | we call union that then calls to find to get root of couple
        
        count = sum([1 for i, a in enumerate(parent) if i == find(a)]) # count number of couples where root is same as couple number | i == find(a) means root of couple is same as couple number
        return n - count # return number of swaps required to make all couples happy