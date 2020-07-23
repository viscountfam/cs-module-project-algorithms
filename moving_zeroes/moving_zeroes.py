'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # for i in range(0, len(arr)):
    #     if arr[i] == 0:
    #         arr.append(arr.pop(i))
    # return arr
    count = arr.count(0)
    arr = list(filter(lambda a: a != 0, arr))
    while count > 0:
        arr.append(0)
        count -= 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")