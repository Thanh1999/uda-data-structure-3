def sort_012(input_list):
    frequency = {}
    result = []
    for element in input_list:
        if frequency.get(element):
            frequency[element] += 1
        else:
            frequency[element] = 1

    for number in range(0, 3, 1):
        if frequency[number]:
            while frequency[number] > 0:
                result.append(number)
                frequency[number] -= 1
    return result

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    print(sorted(test_case))
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
