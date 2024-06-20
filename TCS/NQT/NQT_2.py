def unique_paths(m, n):
    # Create a 2D list for memoization initialized with -1
    dp = [[-1 for _ in range(n)] for _ in range(m)]

    def f(i, j):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        up = f(i - 1, j)
        left = f(i, j - 1)
        dp[i][j] = up + left
        return dp[i][j]
    
    return f(m - 1, n - 1)

if __name__ == "__main__":
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    result = unique_paths(m, n)
    print(f"Number of unique paths from top-left to bottom-right is: {result}")

#the approach is to use recursion and memoization to solve the problem. and logic of this code is to find the number of unique paths from top-left to bottom-right of a m x n grid.