print("********** PROGRAM FOR CALCULATOR **********")
print("ENTER 1 FOR ADDITION:")
print("ENTER 2 FOR SUBSTRACTION:")
print("ENTER 3 FOR MULTIPLICATION:")
print("ENTER 4 FOR DIVISION:")
a=int(input(" ENTER YOUR CHOICE:"))
b = int(input("ENTER FIRST NUMBER:"))
c = int(input("ENTER SECOND NUMBER:"))
if (a==1):
    d = (b+c)
    print("ADDITION = ",d)
elif (a==2):
    d = (b-c)
    print("SUBSTRACTION = ",d)
elif (a==3):
    d = (b*c)
    print("MULTIPLICATION = ",d)
elif (a==4):
    d = (b/c)
    print("DIVISION = ",d)
else:
    print("INVALID INPUT")
    
    
