num = int(input("enter the fibonacci series genarated"))
firstterm = 0
secondterm=1
print("fibonacci series with",num,"term")
print(firstterm,secondterm,end=" ")

for i in range(2,num):
    curterm=firstterm+secondterm
    print(curterm,end="")
    curterm=firstterm
    firstterm=secondterm
    print()
    