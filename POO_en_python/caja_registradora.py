"""Para este proyecto, deberás programar una caja registradora para una almacén. 
El sistema debe poder escanear un producto (el cajero puede tipear el código del producto), 
y agregarlo a la lista de productos comprados para ese cliente. Además debe mostrar el subtotal. 
El cajero cuando lo desee puede finalizar la compra y el sistema deberá aplicar los descuentos correspondientes a los productos. 
Luego, el cajero indica con cuánto paga el cliente y el sistema debe mostrar el cambio que debe devolver al cliente.

Author: Darling Olvera
"""
import unittest

class Producto:

    def __init__(self,codigo):
        self.codigo_precio = {'choco':22, 'coca':18,'sabri':26,'hotd':19}
        self.descuento_producto = 0.0
        self.codigo = codigo
        
    def  aplicar_descuento(self,porcentaje):
        """aplica un descuento al precio base del producto segun un porcentaje dado
            parametros:
                porcentaje = entero que represente el porcentaje de descuento a aplicar
        """
        self.descuento_producto = (self.codigo_precio.get(self.codigo) * porcentaje) / 100
        return self.descuento_producto

class Caja:

    def __init__(self, producto):
        self.compra = list()
        self.descuentos = list()
        self.producto = producto
        self.subtotal = 0
        self.total = 0.0
        self.cambio = 0.0

    def add_product(self, codigo_producto, descuento, cantidad):
        """agrega los precios de los productos y los descuentos de los mismos a aplicar a su respectiva lista
            parametros: 
                codigo_producto = string de cuatro caracteres para identificar al producto
                descuento = descuento que trae el producto
                cantidad = entero para indicar cuanta cantidad del producto se requiere
        """
        p = self.producto.codigo_precio.get(codigo_producto,0) * cantidad
        d = descuento * cantidad
        
        return self.compra.append(p), self.descuentos.append(d)
    
    def calc_subtotal(self):
        "calcula el subtotal en base a la lista de compra"
        for c in self.compra:
            self.subtotal = self.subtotal + c
        return self.subtotal
    
    def aplicar_descuentos(self):
        "aplica los descuentos por producto en base a la lista de descuentos"
        for descuento in self.descuentos:
            self.subtotal = self.subtotal - descuento
        self.total = self.subtotal
        return self.total
    
    def regresar_cambio(self,cantidad_pagada):
        """regresa el cambio de la cantidad con la que se pago
            parametros:
                cantidad_pagada = cantidad con la que pagó el cliente"""
        self.cambio = cantidad_pagada - self.total
        return self.cambio
    

    
class TestCajaRegistradora(unittest.TestCase):

    
    def test_metodo_aplicar_descuento(self):
        producto1 = Producto('choco')
        producto1.aplicar_descuento(50)
        self.assertEqual(producto1.descuento_producto,11.0)

    def test_metodo_add_product(self):
        producto1 = Producto('choco')
        producto2 = Producto('coca')
        compra1 = Caja(producto1)
        compra1 = Caja(producto2)
        cantidad = 2
        compra1.add_product(producto1.codigo,producto1.descuento_producto ,cantidad)
        compra1.add_product(producto2.codigo,producto2.descuento_producto,1)
        #cantidad correcta de productos ingresados
        self.assertEqual(len(compra1.compra), 2)
        self.assertEqual(len(compra1.descuentos), 2)  
        #precios correctos segun el codigo de producto
        self.assertEqual(compra1.compra[0],22*cantidad) 
        self.assertEqual(compra1.compra[1],18)
    
    def test_metodo_calc_subtotal(self):
        producto1 = Producto('choco')
        producto2 = Producto('coca')
        compra1 = Caja(producto1)
        compra1 = Caja(producto2)
        compra1.add_product(producto1.codigo,producto1.descuento_producto,2)
        compra1.add_product(producto2.codigo,producto2.descuento_producto,2)
        #suma correctamente los valores dentro de la lista compra
        self.assertEqual(compra1.calc_subtotal(),80)

    def test_metodo_aplicar_descuentos(self):
        producto1 = Producto('choco')
        producto1.aplicar_descuento(50)
        producto2 = Producto('sabri')
        producto2.aplicar_descuento(50)
        compra1 = Caja(producto1)
        compra1 = Caja(producto2)
        compra1.add_product(producto1.codigo,producto1.descuento_producto,1)
        compra1.add_product(producto2.codigo,producto2.descuento_producto,1)
        compra1.calc_subtotal()
        #devuelve correctamente el total con el descuento aplicado
        self.assertEqual(compra1.aplicar_descuentos(),24.0)

    def test_metodo_regresar_cambio(self):
        producto1 = Producto('choco')
        producto2 = Producto('coca')
        compra1 = Caja(producto1)
        compra1 = Caja(producto2)
        compra1.add_product(producto1.codigo,producto1.descuento_producto,2)
        compra1.add_product(producto2.codigo,producto2.descuento_producto,2)
        compra1.calc_subtotal()
        compra1.aplicar_descuentos()
        #regresa correctamente el cambio de pagar con 100 pesos
        self.assertEqual(compra1.regresar_cambio(100),20)


        

    

