from datetime import date
perName = input("enter the name of the prson")
perDOB =int(input("enter thr birth year"))
curyear = date.today().year
perage = curyear-perDOB
if ("age>60"):
    print(perName,"age",perage, "is not a senior citizen")
else:
    print(perName,"age",perage,"is  senior citizen") 
    