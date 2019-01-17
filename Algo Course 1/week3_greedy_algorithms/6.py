#Uses python3

import sys
def IsGreaterOrEqual(digit, maxDigit):
    temp=""
    temp1=""
    temp=str(digit)+str(maxDigit)
    temp1=str(maxDigit)+str(digit)
    if int(temp)>int(temp1):
        return True
    else:
        return False
def largest_number(a):
    res = ""
    while len(a)>0:
        maxDigit = 0
        for digit in a:
            if IsGreaterOrEqual(digit, maxDigit):
                maxDigit=digit
        res=res+str(maxDigit)
        a.remove(maxDigit)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
