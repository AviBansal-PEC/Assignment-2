a=int(input("Enter Length of Side 1:"))
b=int(input("Enter Length of Side 2:"))
c=int(input("Enter Length of Side 3:"))
if a+b>c and b+c>a and c+a>b:
    print("Yes")
else:
    print("No")