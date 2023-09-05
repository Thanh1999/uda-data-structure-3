def get_min_max(ints):
    if not ints:
        return None
    
    min = ints[0]
    max = ints[0]

    for i in range(1, len(ints), 1):
        if ints[i] > max:
            max = ints[i]
        if ints[i] < min:
            min = ints[i]

    return min, max

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print("---Test cases---")
### Case list is valid
l1 = [10, 8, 11, 23, 100, 40, 1, 99]
print(get_min_max(l1))
# Expect (1, 100)

### Case list is empty
print(get_min_max([]))
# Expect None

### Case list is None
print(get_min_max(None))
# Expect None