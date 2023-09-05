def find_sqrt_number(begin, end, number):
    if begin > end:
        return None
    
    half = (begin + end) // 2
    sqr = half * half
    
    if sqr == number:
        return half
    if sqr > number:
        return find_sqrt_number(begin, half - 1, number)
    else:
        return find_sqrt_number(half + 1, end, number)

def sqrt(number):
    if number:
        return find_sqrt_number(0, number, number)

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

print("---Test cases---")
### Case find int square root
print(sqrt(25))
# Expect 5
print(sqrt(81))
# Expect 9

### Case not find int square root
print(sqrt(7))
# Expect None

### Case pass negative or None number
print(sqrt(-16))
# Expect None