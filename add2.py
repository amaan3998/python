ef add2(a,b):
    c=a.__add__(b)
    return c

def main():
    s=int(input("Enter 1st number:"))
    p=int(input("Enter 2nd number:"))
    x=add2(s,p)
    print(x)

main()
~
