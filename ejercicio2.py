numero=int(input("ingrese un numero:"))
if numero%2==0:
    print("el numero es par")
else:
    print("el numero es impar")

print("el numero es par" if numero%2==0 else "el numero es impar")