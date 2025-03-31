def binary_search(numbers, target):
    first = 0
    last = len(numbers) - 1
    
    while first <= last:
        midpoint = (first + last) // 2
        if numbers[midpoint] == target:
            return midpoint
        elif numbers[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return None

def verify_search(expected_index):
    """
    Verify the result of the binary search.
    """
    if expected_index is not None:
        print(f"Target found at index: {expected_index}")
    else:
        print("Target not found in the list.")
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(numbers, 5)
verify_search(binary_search(numbers, 5))
binary_search(numbers, 11)
verify_search(binary_search(numbers, 11))