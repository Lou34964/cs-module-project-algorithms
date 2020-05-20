'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    return sliding_window_max_unoptimized(nums, k)
    # return sliding_window_max_optimized(nums, k)
    
def sliding_window_max_unoptimized(nums, k):
    total_maxes = len(nums) - k + 1
    maxes = [None] * total_maxes

    for i in range(total_maxes):

        lower = i
        upper = i + (k - 1)
        maxes[i] = max(nums[lower:upper + 1])
    
    return maxes


def sliding_window_max_optimized(nums, k):
    maxes = []

   
    max_value = nums[0]
    max_index = 0

    second_largest = None
    second_largest_index = None


    for i in range(len(nums)):


        if i < k:

            if nums[i] > max_value:
                max_value = nums[i]
                max_index = i
        else:
            pass

    return maxes
if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
