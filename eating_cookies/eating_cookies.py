'''
Input: an integer
Returns: an integer
'''

# def index_in_list(arr, index):
#     return index < len(arr)
# def eating_cookies(n, cache=None):
#     # Your code here
#     # since were going to be using recursion 
#     # we need a list to hold precalculated values and not exceed the call stack
#     cookies = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064]
#     if cache is None:
#         cache = cookies + [0 for i in range(len(cookies), n + 1)]
#     for i in range(0, n + 1):
#         if index_in_list(cookies, i):
#             cache[i] = cookies[i]
#      # calculating the next value of n is done by adding the last three n values together
#     if cache[n] != 0:
#         return cache[n]
#     else:
#         cache[n] = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
#         return cache[n]

def eating_cookies(n, cache=None):
    # base cases
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the work has already been done
    # by looking in the cache
    elif cache is not None and cache[n] > 0:
        # return the previously computed answer and don't recurse
        return cache[n]
    else:
        # might need to create our cache for the first time
        if cache is None:
            # initialize an empty list for a cache
            cache = [0 for i in range(n+1)]
        # store the value of the recursive call expressions in our cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    
    return cache[n]



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 12

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
 
