class InsertInterval:

    # O(LogN)
    # def insert_interval(self, interval_list, new_interval):
    #     # Append the new interval
    #     interval_list.append(new_interval)
    #     interval_list.sort(key=lambda i: i[0])

    #     output_list = [interval_list[0]]

    #     for first, last in interval_list[1:]:
    #         last_element = output_list[-1][1]
    #         if last_element >= first:
    #             output_list[0][1] = max(last_element, last)
    #         else:
    #             output_list.append([first, last])
    #     return output_list

    # O(N)

    def insert_interval_efficient(self, interval_list, new_interval):
        res = []

        for i in range(len(interval_list)):

            # Non-merging - insert to left
            if new_interval[1] < interval_list[i][0]:
                res.append(new_interval)
                # Return the result immediately as no other element on the right will overlap
                return res + interval_list[i:]

            # Non-merging - insert to right
            elif new_interval[0] > interval_list[i][1]:
                res.append(interval_list[i])
            # Merging condition - overlap
            else:
                new_interval = [min(interval_list[i][0], new_interval[0]),
                                max(interval_list[i][1], new_interval[1])]

        # Append the merged or right-side non-overlapping new_interval
        res.append(new_interval)

        return res


# Example usage
insertInterval = InsertInterval()
result = insertInterval.insert_interval_efficient([[1, 3], [6, 9]], [2, 5])
print(result)  # Output: [[1, 5], [6, 9]]
