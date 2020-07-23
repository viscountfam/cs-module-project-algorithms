'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # beginning = 0
    # end = k + 1
    # window = nums[beginning : end]
    # local_maxima = []
    # while True:
    #      local_maxima.append(max(window))
    #      beginning += 1
    #      end += 1
    #      window = nums[beginning : end]
    #      if window[-1] == nums[-1]:
    #         local_maxima.append(max(window))
    #         beginning += 1
    #         end += 1
    #         window = nums[beginning : end]
    #         break
    # return local_maxima
    res = []
    for i in range(0, len(nums)):
        arr = nums[i:i+k]

        if len(arr) == k:
            res.append(max(arr))
    return res


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
