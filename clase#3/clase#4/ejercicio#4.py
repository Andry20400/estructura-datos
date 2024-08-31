import random
def generar_contrasena(longitud): 
    caracteres = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890@$"
    contrasena = ""
    for _ in range(longitud):
        contrasena += random.choice(caracteres) 
    return contrasena 
nueva_contrasena = generar_contrasena(8) 
print (nueva_contrasena) 
