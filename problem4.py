def sort_012(input_list):
    if not input_list:
        return
    
    begin = 0
    mid = 0
    end = len(input_list) - 1

    while mid <= end:
        if input_list[mid] == 0:
            input_list[begin], input_list[mid] = input_list[mid], input_list[begin]
            begin += 1
            mid += 1
        elif input_list[mid] == 1:
            mid += 1
        else:  # input_list[mid] == 2
            input_list[mid], input_list[end] = input_list[end], input_list[mid]
            end -= 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

### Case can sort correctly
print(sort_012([2, 0, 2, 0, 1, 2, 1, 0, 1, 0]))
# Expect [0, 0, 0, 0, 1, 1, 1, 2, 2, 2]

### Case list is empty
print(sort_012([]))
# Expect None

### Case list is None
print(sort_012(None))
# Expect None