'''
Input: an integer
Returns: an integer
'''

def index_in_list(arr, index):
    return index < len(arr)
def eating_cookies(n):
    # Your code here
    # since were going to be using recursion 
    # we need a list to hold precalculated values and not exceed the call stack
    cookies = [1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064]
    # calculating the next value of n is done by adding the last three n values together
    if index_in_list(cookies, n):
        return cookies[n]
    else:
        total_cookies = eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
        cookies.append(total_cookies)
        return total_cookies
        


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

