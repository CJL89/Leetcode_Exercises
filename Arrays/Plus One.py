digits = [1,2,3]
digits1 = [1,2,3,4,5,9,8]
digits2 = [9,9]
digits3 = [0,0,0]
digits4 = [0]
digits5 = [1,0]
digits6 = [8,9,4,5,0,0,7,10]

def plusOne(digits):

    for i in range(len(digits)):
        if len(digits) != 1 and digits[i] == 0 and digits[i-1] == 0:
            lastDigit = digits[-1] + 1
            digits[-1] = lastDigit
            return digits
        if digits[-1] >= 10:
            digits[-2] = digits[-2] + 1
            digits[-1] = 0
            return digits
        else:
            digits = ''.join(map(str, digits))
            intDigits = str(int(digits) + 1)
            return [x for x in intDigits]


print(plusOne(digits6))
