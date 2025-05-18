def saludar(nombre): 
    print("Hola " + nombre) 
 
saludar("Mundo") 

def dividir(a, b):
    try:
        R = a / b
    except ZeroDivisionError:
        print("no se puede dividir entre cero")
        R = None
    return R

print(dividir(10, 0)) 