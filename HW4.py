class Museum:
    def __init__(self, value: list[int], weight: list[int], c_max: int):
        #these are my instance varaibles
        #we added an extra for n becuase we want to make sure we ignore index 0
        self.value = value
        self.weight = weight
        self.c_max = c_max
        self.n = len(value) - 1

 

    def __optimal_subset_value(self, value:list[int], weight:list[int], Cmax:int) -> list[list[int]]:
        """
        Pseudocode for S
        Initialize array with n+1 rows and Cmax+1 columns
        Set first row and first column to 0
        for row = 1 to n inclusive:
        for avail_capacity = 1 to Cmax inclusive:
         ... etc etc ...
        """
        #Then we make sure that we store zero at the first row and column
        #And when we do this we want to skip the first index 
        #and doing len(value) - 1 so that when we iterate it will 
        #correclty go to the correct spot that is actually occupied by a value
        n = len(value) - 1
        rows = Cmax + 1
        S = [[0] * rows for _ in range(n + 1)]
        for row in range(1, n + 1):
            for avail_capacity in range(1, Cmax + 1):
                #we check if the weight is greater then capacity
                if weight[row] > avail_capacity:
                    #We dont include and item
                    S[row][avail_capacity] = S[row-1][avail_capacity]
                else:
                    #If the weight dosent exceed capcity we can decide to skip the item or we want to take it. 
                    S[row][avail_capacity] = max(S[row-1][avail_capacity], S[row-1][avail_capacity - weight[row]] + value[row])


        return S


    def __build_subset(self, S: list[list[int]]):
        #When we do this we ant to make sure that we start at the bottom right
        subset = []
        items, capacity = self.n, self.c_max
        #we start iterating until items and capacity are both gone
        while items > 0 and capacity >0:
            #Then we check if therer is a difference of values in the previous row
            if S[items][capacity] != S[items-1][capacity]:
                #if there is include item 
                subset.append(items)
            #and decrease the capacity
            capacity -= self.weight[items]
            #Then we want to continue backwards
            items -= 1
        #This will give us the orginal order.
        return subset[::-1]
        # iterate backwards through S to find which items are included
        # ... your code here ...
    

    def solve(self):
        ##We first find the opttimal subset value
        find_optimal_subset = self.__optimal_subset_value(self.value, self.weight, self.c_max)
        print(find_optimal_subset)
        #then we find the we build the subset
        find_items = self.__build_subset(find_optimal_subset)
        print(find_items)
        #we then want to find the total number of subset 
        max_num_subsets = 2 ** self.n
        print(max_num_subsets)
        #size of matrix table
        size_matrix = (self.n + 1) * (self.c_max)
        print(size_matrix)
        #Finding the max weight and total value
        max_weight =  sum(self.weight[i] for i in find_items)
        print(max_weight)
        total_value = sum(self.value[i] for i in find_items)
        print(total_value)


    

value  = [None, 10, 5, 16, 11]
weight = [None, 3, 2, 4, 4]
c_max  = 10

result = Museum(value, weight, c_max)
result.solve()