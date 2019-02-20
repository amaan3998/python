def add_frac(num1, den1, num2, den2):
    den = den1*den2
    num = (num1*den2)+(num2*den1)
    return num, den

def main():
    num, den = add_frac(1, 2, 1, 3)
    print("%d%d + %d%d is %d/%d" %(1, 2, 1, 3, num, den))

main()
