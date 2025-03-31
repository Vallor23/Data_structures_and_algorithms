def linear_search(numbers,target):
    """
    Perform a linear search on the list of numbers to find the target number.
    """
    for i in range(0, len(numbers)):
        if numbers[i] == target:
            return i
    return None

def verify_search(expected_index):
    """
    Verify the result of the linear search.
    """
    if expected_index is not None:
        print(f"Target found at index: {expected_index}")
    else:
        print("Target not found in the list.")
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linear_search(numbers, 5)
verify_search(linear_search(numbers, 5))
linear_search(numbers, 11)
verify_search(linear_search(numbers, 11))