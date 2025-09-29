a=input("Dona'm un número: ")
b=input("Dona'm un número: ")
print("Tipus de dada" , type(a))
if(a.isnumeric() and b.isnumeric() ):
    print("Dins el IF")
    c=a+b
    print("Sumade",a,"i",b, "és", c)
else:
    print("Dins el ELSE")
    print("No és un número")

print("Final")