a=int(input("how many units you want to buy"))
b=a*100
c=b*10/100
if b>1000:
    d=b-c
    print("your discount is:", c)
    print("total amount to be paid:", d )
else:
    print("total amount to be paid:", b)


