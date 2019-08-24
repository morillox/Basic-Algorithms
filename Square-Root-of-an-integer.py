def sqrt(number):
    if number < 0:
        return None

    return SRT(0, number, number, None)

def SRT(left, right, numbef, checknum):
    if left > right:
        return checknum

    mid = left + (right - left) // 2
    mult = mid * mid

    if mult > numbef:
        return SRT(left, mid - 1, numbef, checknum)
    elif mult == numbef:
        return mid
    else:
        return SRT(mid + 1, right, numbef, mid)


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")