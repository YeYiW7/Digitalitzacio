print("Programa que em diu si un numero es parell o senar")
num=input("Introdueix un numero sencer:")
if(num.isnumeric()):
    print("no és numèric")
    # print(type(num))
    reste = int(num) % 2
    if reste == 0:
        print(num, " és parrel")
    else: # if reste == 1:
        print(num," és senar")
else:
    print("Error: Has d'introduir un numero sencer")