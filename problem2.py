def rotated_array_search(input_list, number):
    begin = 0
    end = len(input_list) - 1

    while begin <= end:
        half = (begin + end) // 2
        if input_list[half] == number:
            return half

        # Check if the left half is sorted
        if input_list[begin] <= input_list[half]:
            if input_list[begin] <= number < input_list[half]:
                end = half - 1
            else:
                begin = half + 1
        # Otherwise, the right half must be sorted
        else:
            if input_list[half] < number <= input_list[end]:
                begin = half + 1
            else:
                end = half - 1
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])