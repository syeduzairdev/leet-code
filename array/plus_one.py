def plusOne(digits):
    n = len(digits)
    
    # Start from the last digit
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    
    # If we are here, all digits were 9
    # So we need to add a 1 at the beginning
    return [1] + digits


print(plusOne([1,2,3]))     # [1,2,4]
print(plusOne([4,3,2,1,8,1,8]))   # [4,3,2,2]
print(plusOne([1]))     # [1,0,0,0]    