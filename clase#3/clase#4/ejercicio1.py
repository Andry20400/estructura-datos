def operar (num1, num2, operacion ): 
     if operacion == 'suma': 
        return num1 + num2 
     elif operacion == 'resta':
         return num1 - num2 
     elif operacion == 'multiplicacion':
         return num1 * num2 
     elif operacion == 'division':
       if num2 != 0: 
          return num1 / num2
     else:
        return "Error: division entre cero"
print ("suma", operar(15, 5, 'suma'))
print ("resta", operar(10, 8, 'resta'))
print ("multiplicacion", operar(10, 5, 'multiplicacion'))
print ("division", operar(4, 2, 'division'))
