def numSquares(n):
    """
    Given an integer n, return the least number of perfect square numbers 
    that sum to n.
    """
    # Base cases
    if n < 4:
        return n
    
    # Initialize a list to store the minimum number of squares for each number
    dp = [0] * (n + 1)
    
    # Initialize the first 4 elements
    for i in range(1, 4):
        dp[i] = i
    
    # Iterate through the remaining numbers
    for i in range(4, n + 1):
        # Find the minimum number of squares that sum up to i
        min_squares = i
        j = 1
        while j * j <= i:
            min_squares = min(min_squares, 1 + dp[i - j * j])
            j += 1
        dp[i] = min_squares
    
    return dp[n]


print(numSquares(13))
