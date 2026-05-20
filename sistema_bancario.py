from random import randint
"""
Práctica de programación orientada a objetos con python:
 -Sistema bancario simple en python
"""

# CLASES


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido,  num_cuenta, balance):
        super().__init__(nombre, apellido)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def showData(self):
        return f"""
            Cliente: {self.nombre} {self.apellido}
            No de cuenta: {self.num_cuenta}
            Saldo disponible: {self.balance} 
        """

    def depositar(self):
        cantidad = input("Ingrese la cantidad a depositar: ")
        self.balance = self.balance + float(cantidad)
        return f"Saldo nuevo: {self.balance}"

    def retirar(self):
        cantidad = input("Ingrese la cantidad a retirar: ")
        if (self.balance <= 0 or self.balance - float(cantidad) < 0):
            return "No tiene saldo suficiente"
        else:
            self.balance = self.balance - float(cantidad)
            return f"Saldo restante: {self.balance}"

# FUNCIONES


def crear_cliente(nombre, apellido):
    numeros = []
    for n in range(1, 17):
        n = randint(0, 10)
        numeros.append(n)
    cuenta = ''.join(str(n) for n in numeros)

    new_client = Cliente(nombre, apellido, cuenta, 0.0)

    return new_client


def print_menu():
    print("OPCIONES DISPONIBLES\n")
    print("""
          1 - Consultar información
          2 - Depositar
          3 - Retirar
          4 - Salir del sistema
          """)
    option = input("\n Ingrese el numero de la opción que le interesa: ")
    return int(option)


def main():

    print("=" * 20)
    print("SISTEMA BANCARIO")
    print("=" * 20)

    nombre = input("Ingresa tu primer nombre: ")
    apellido = input("Ingresa tu primer apellido: ")

    cliente = crear_cliente(nombre, apellido)

    cliente.showData()

    opcion = print_menu()

    while opcion != 4:
        if opcion == 1:
            print(cliente.showData())
        elif opcion == 2:
            new_balance = cliente.depositar()
            print(new_balance)
        elif opcion == 3:
            new_balance = cliente.retirar()
            print(new_balance)
        opcion = print_menu()


main()
