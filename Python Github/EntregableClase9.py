#FORMA 1- Pasando numero hardcodeado por parametro

def año_bisiesto(año):
    if type(año) != int:
        print("No estas ingresando un numero!")
    elif año%4==0 and (año%100 == 0 or not año%400 ==0): #es bisiesto
        print(f"Si! El año {año} es bisiesto!")
    else:
        print(f"No.. {año} no es bisiesto")

año_bisiesto(1976) 




#FORMA 2- Usando un input

año = input("Ingrese un numero: ")

def año_bisiesto(año):
    if año.isdigit():
        año = int(año)
        if año%4==0 and (año%100 == 0 or not año%400 ==0): #es bisiesto
            print(f"Si! El año {año} es bisiesto!")
        else:
            print(f"No.. {año} no es bisiesto")
    else:
        año = input("Ingrese un numero: ")
        año_bisiesto(año)
    

año_bisiesto(año)