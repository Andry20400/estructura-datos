peso = input(int("ingrese su peso en kilogramos:"))
estatura = input(int("ingrese su estatura"))

IMC = peso / (estatura * estatura)

if IMC >25:
print("esta en sobre peso")

if IMC <18.5:
print("su peso es normal")
