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

# Case find int square root
assert 5 == sqrt(25)
assert 9 == sqrt(81)

# Case not find int square root
assert None == sqrt(7)
assert None == sqrt(13)

# Case pass negative or None number
assert None == sqrt(-16)
assert None == sqrt(None)