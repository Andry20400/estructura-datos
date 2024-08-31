def es_polindromo(palabra): 
    palabra_limpia = palabra.replace("","").lower()
    return palabra_limpia == palabra_limpia [::-1]
def main ():    
    palabra = input("escribe una palabra para verificar si es polindromo:")
    if es_polindromo(palabra): 
     print(f"'{palabra}' es un polindromo")
    else: 
       print(f"'{palabra}' no es un polindromo")
if __name__== "__main__":
    main ()