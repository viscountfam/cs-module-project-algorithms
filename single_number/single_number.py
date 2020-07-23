'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    counts = {}
    for n in arr:
        if n not in counts:
            counts[n] = 0
        counts[n] += 1
    
    singles = []
    for n, count in sorted(counts.items()):
        if count == 1:
            singles.append(n)

    return singles[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")