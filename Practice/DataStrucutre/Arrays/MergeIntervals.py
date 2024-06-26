# def merge_intervals(intervals):
#     # Step 1: Sort the intervals by their starting points
#     intervals.sort(key=lambda x: x[0])

#     # Step 2: Initialize the list to hold the merged intervals
#     merged = []

#     for interval in intervals:
#         # If merged is empty or current interval does not overlap with the previous, append it
#         if not merged or merged[-1][1] < interval[0]:
#             merged.append(interval)
#         else:
#             # There is an overlap, so merge the current interval with the previous one
#             merged[-1][1] = max(merged[-1][1], interval[1])

#     return merged


# # Example usage
# intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
# output1 = merge_intervals(intervals1)
# print(output1)  # Output: [[1, 6], [8, 10], [15, 18]]

# intervals2 = [[1, 4], [4, 5]]
# output2 = merge_intervals(intervals2)
# print(output2)  # Output: [[1, 5]]


def merge_interval(input_list: list):
    input_list.sort(key=lambda i: i[0])

    output_list = [input_list[0]]

    for start, end in input_list[1:]:
        last_element = output_list[-1][-1]

        if last_element >= start:
            output_list[0][-1] = max(last_element, end)
        else:
            output_list.append([start, end])
    return output_list


print(merge_interval([[1, 3], [2, 6], [8, 10], [15, 18]]))
