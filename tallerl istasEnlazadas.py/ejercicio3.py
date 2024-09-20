class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def __str__(self):
        return f"{self.tipo} - {self.nombre}, Edad: {self.edad} años"

class Nodo:
    def __init__(self, animal):
        self.animal = animal
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def agregar_animal(self, animal):
        if self.existe(animal):
            print(f"El animal {animal.nombre} ya está en la lista.")
            return
        
        nuevo_nodo = Nodo(animal)
        
        if not self.head:  
            self.head = nuevo_nodo
            return
        actual = self.head
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def existe(self, animal):
        actual = self.head
        while actual:
            if actual.animal.nombre == animal.nombre:
                return True
            actual = actual.siguiente
        return False

    def mostrar_lista_recursiva(self, nodo):
        if nodo is None:
            return
        print(nodo.animal)
        self.mostrar_lista_recursiva(nodo.siguiente)

    def mostrar_lista_bucle(self):
        actual = self.head
        while actual:
            print(actual.animal)
            actual = actual.siguiente

def main():
    lista_animales = ListaEnlazada()

    aguila = Animal("Águila Real", 5, "Águila")
    pantera = Animal("Pantera Negra", 3, "Pantera")
    vaca = Animal("Vaca Lechera", 4, "Vaca")
  
    lista_animales.agregar_animal(aguila)
    lista_animales.agregar_animal(pantera)
    lista_animales.agregar_animal(vaca)

    lista_animales.agregar_animal(aguila)
    print("Animales en la lista (usando bucle):")
    lista_animales.mostrar_lista_bucle()

    print("\nAnimales en la lista (usando recursión):")
    lista_animales.mostrar_lista_recursiva(lista_animales.head)

if __name__ == "__main__":
    main()
