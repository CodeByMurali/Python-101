# Leet code 75
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.


# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

def sortColors(nums):
    # Initialize pointers for red, white, and blue sections
    red, white, blue = 0, 0, len(nums) - 1

    # Iterate through the array
    while white <= blue:
        if nums[white] == 0:  # If current element is red
            nums[red], nums[white] = nums[white], nums[red]
            red += 1
            white += 1
        elif nums[white] == 1:  # If current element is white
            white += 1
        else:  # If current element is blue
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1

    return nums


# Test cases
nums1 = [2, 0, 2, 1, 1, 0]
nums2 = [2, 0, 1]

print(sortColors(nums1))  # Output: [0, 0, 1, 1, 2, 2]
print(sortColors(nums2))  # Output: [0, 1, 2]
