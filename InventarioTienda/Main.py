from Services.ProductServices import ProductServices
from Ui.Menu import mostrar_menu

def main():
    inventario = ProductServices()

    while True:
        mostrar_menu()
        opcion = input(" Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)

        elif opcion == "2":
            inventario.mostrar_inventario()

        elif opcion == "3":
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)

        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(nombre, nueva_cantidad)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
