def search_rotated_array(arr, target):
    # Right is set to len(arr) - 1 because of zero-based indexing
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # If the target is found, return the index

        # Determine which side is normally ordered
        if arr[left] <= arr[mid]:  # Left side is normally ordered
            if arr[left] <= target < arr[mid]:
                right = mid - 1  # Target is in the left side
            else:
                left = mid + 1  # Target is in the right side
        else:  # Right side is normally ordered
            if arr[mid] < target <= arr[right]:
                left = mid + 1  # Target is in the right side
            else:
                right = mid - 1  # Target is in the left side

    return -1  # Target not found


# Example usage
arr = [5, 6, 7, 1, 2, 3, 4]
target = 3
index = search_rotated_array(arr, target)
print(index)  # Output: 5
