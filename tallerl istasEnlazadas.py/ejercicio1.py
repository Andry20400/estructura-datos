class Nodo:
    def _init_(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaSimple:

    def _init_(self):
        self.primero = None

    def esta_vacia(self):
        return self.primero is None

    def insertar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            nodo_actual = self.primero
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def mostrar(self):
        nodo_actual = self.primero
        while nodo_actual is not None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

    def remover(self, valor):
        if self.esta_vacia():
            return

        if self.primero.valor == valor:
            self.primero = self.primero.siguiente
            return
        
        nodo_actual = self.primero
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.valor == valor:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return
            nodo_actual = nodo_actual.siguiente

    def encontrar(self, valor_a_buscar):
        nodo_actual = self.primero
        indice = 0
    
        while nodo_actual is not None:
            if nodo_actual.valor == valor_a_buscar:
                return f"El valor {valor_a_buscar} está en la posición {indice}."
            nodo_actual = nodo_actual.siguiente
            indice += 1
        
        return f"El valor {valor_a_buscar} no se encuentra en la lista."

lista = ListaSimple()

print("Insertando valores en la lista:")
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)

print("Contenido de la lista:")
lista.mostrar()
valor_a_buscar = 20
resultado_busqueda = lista.encontrar(valor_a_buscar)
print(resultado_busqueda)
valor_no_encontrado = 40
resultado_busqueda = lista.encontrar(valor_no_encontrado)
print(resultado_busqueda)