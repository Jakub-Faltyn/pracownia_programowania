a=int(input("Enter number: "))
qt=0
sum=0
mean=0
while a!=0:
    sum=sum+a
    qt=qt+1
    a=int(input("Enter number: "))
mean=sum/qt
print(f"RESULT: Quantity={qt}, Sum={sum}, Mean={mean}")