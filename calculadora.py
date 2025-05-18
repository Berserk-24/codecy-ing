def saludar(nombre): 
    print("Hola " + nombre) 
 
def dividir(a, b): 
    return a / b 
 
saludar("Mundo") 

print(dividir(10, 0)) 

def dividir(a, b):
    try:
        R = a / b
    except ZeroDivisionError:
        print("no se puede dividir entre cero")
        R = None
    return R