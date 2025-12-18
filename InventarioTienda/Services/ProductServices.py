from Models.Product import Product
from typing import List, Optional


class ProductServices:
    """
    Clase para gestionar el inventario de productos.

    """
    
    def __init__(self):
        self.productos: List[Product] = []

    def agregar_producto(self, nombre: str, cantidad: int, precio: float) -> bool:

        if not nombre or nombre.strip() == "":
            print("Error: El nombre del producto no puede estar vacío.")
            return False
        
        if not isinstance(cantidad, int) or cantidad < 0:
            print("Error: La cantidad debe ser un número entero positivo o cero.")
            return False
        
        if not isinstance(precio, (int, float)) or precio < 0:
            print("Error: El precio debe ser un número positivo o cero.")
            return False
        
        if self._buscar_producto(nombre):
            print(f"Error: El producto '{nombre}' ya existe en el inventario.")
            return False
        
        self.productos.append(Product(nombre, cantidad, precio))
        print(f"✓ Producto '{nombre}' agregado correctamente.")
        return True

    def mostrar_inventario(self) -> None:
        
        if not self.productos:
            print("El inventario está vacío.")
            return
        
        """ REPASAR """
        print("\n" + "="*50)
        print("INVENTARIO DE PRODUCTOS")
        print("="*50)
        for i, product in enumerate(self.productos, 1):
            print(f"{i}. {product}")
        print("="*50 + "\n")
 
    def eliminar_producto(self, nombre: str) -> bool:
        if not nombre or nombre.strip() == "":
            print("Error: Debe proporcionar un nombre de producto.")
            return False
        
        producto = self._buscar_producto(nombre)
        if producto:
            self.productos.remove(producto)
            print(f"✓ Producto '{nombre}' eliminado correctamente.")
            return True
        
        print(f"Error: Producto '{nombre}' no encontrado en el inventario.")
        return False

    def actualizar_cantidad(self, nombre: str, nueva_cantidad: int) -> bool:
       
        if not nombre or nombre.strip() == "":
            print("Error: Debe proporcionar un nombre de producto.")
            return False
        
        if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
            print("Error: La cantidad debe ser un número entero positivo o cero.")
            return False
        
        producto = self._buscar_producto(nombre)
        if producto:
            cantidad_anterior = producto.cantidad
            producto.cantidad = nueva_cantidad
            print(f"✓ Cantidad de '{nombre}' actualizada: {cantidad_anterior} → {nueva_cantidad}")
            return True
        
        print(f"Error: Producto '{nombre}' no encontrado en el inventario.")
        return False
    
    def _buscar_producto(self, nombre: str) -> Optional[Product]:
       
        for product in self.productos:
            if product.nombre.lower() == nombre.lower():
                return product
        return None
    
    def obtener_total_productos(self) -> int:
     
        return len(self.productos)
    
    def obtener_valor_total_inventario(self) -> float:
      
        return sum(product.cantidad * product.precio for product in self.productos)