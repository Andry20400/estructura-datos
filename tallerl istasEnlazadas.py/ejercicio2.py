class NodoTarea:
    def _init_(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.siguiente = None  


class ListaTareas:
    def _init_(self):
        self.inicio = None  

    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        nueva_tarea = NodoTarea(descripcion, prioridad, fecha_vencimiento)
        if not self.inicio:
            
            self.inicio = nueva_tarea
        else:
           
            actual = self.inicio
            while actual.siguiente:  
                actual = actual.siguiente
            actual.siguiente = nueva_tarea

    def eliminar_tarea(self, descripcion):
        actual = self.inicio
        previo = None
        while actual:
            if actual.descripcion == descripcion:
                if previo:
                    previo.siguiente = actual.siguiente  
                else:
                    self.inicio = actual.siguiente  
                print(f"Tarea '{descripcion}' eliminada.")
                return
            previo = actual
            actual = actual.siguiente
        print(f"No se encontró la tarea: {descripcion}")

    def mostrar_tareas(self):
        if not self.inicio:
            print("La lista de tareas está vacía.")
            return
        actual = self.inicio
        print("Tareas:")
        while actual:
            print(f"- Descripción: {actual.descripcion}, Prioridad: {actual.prioridad}, Vence: {actual.fecha_vencimiento}")
            actual = actual.siguiente

    def buscar_tarea(self, descripcion):
        actual = self.inicio
        while actual:
            if actual.descripcion == descripcion:
                print(f"Tarea encontrada: Descripción: {actual.descripcion}, Prioridad: {actual.prioridad}, Vence: {actual.fecha_vencimiento}")
                return
            actual = actual.siguiente
        print(f"Tarea '{descripcion}' no encontrada.")
    def marcar_completada(self, descripcion):
        self.eliminar_tarea(descripcion)


def mostrar_menu():
    print("\n1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar todas las tareas")
    print("4. Buscar tarea")
    print("5. Marcar tarea como completada")
    print("6. Salir")

lista_tareas = ListaTareas()

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        descripcion = input("Descripción de la tarea: ")
        prioridad = input("Prioridad (1=Alta, 3=Baja): ")
        fecha_vencimiento = input("Fecha de vencimiento (formato: DD/MM/AAAA): ")
        lista_tareas.agregar_tarea(descripcion, prioridad, fecha_vencimiento)

    elif opcion == "2":
        descripcion = input("Descripción de la tarea a eliminar: ")
        lista_tareas.eliminar_tarea(descripcion)

    elif opcion == "3":
        lista_tareas.mostrar_tareas()

    elif opcion == "4":
        descripcion = input("Descripción de la tarea a buscar: ")
        lista_tareas.buscar_tarea(descripcion)

    elif opcion == "5":
        descripcion = input("Descripción de la tarea a marcar como completada: ")
        lista_tareas.marcar_completada(descripcion)

    elif opcion == "6":
        print("¡Saliendo del programa!")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")