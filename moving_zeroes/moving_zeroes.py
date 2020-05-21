'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    #remove the zero value elements from the list via looping over each value and checking 
    # if it is 0
    nonzero_ints = [number for number in arr if number is not 0]

    #add each 0 removed back to the end of the list. via check the difference is the length
    # of the two lists and adding a zero for each.
    return nonzero_ints + [0] * (len(arr) - len(nonzero_ints))


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")