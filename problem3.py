def rearrange_digits(input_list):

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

    def merge(left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] >= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged

    # Step 1: Convert the input list into a list of strings
    input_list = list(map(str, input_list))

    # Step 2: Sort the list of strings using merge sort
    sorted_list = merge_sort(input_list)

    # Step 3: Join the sorted list of strings to form two numbers
    print(sorted_list)
    number1 = int(''.join(sorted_list[::2]))
    number2 = int(''.join(sorted_list[1::2]))

    # Step 4: Return the two numbers as a list
    return [number1, number2]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)