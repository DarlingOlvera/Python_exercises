#Modelado de problema 1

class Currency(object):
    "Represents a currency"

    # el metodo __init__ se llama cuando se inicializa la clase. 
    # en este metodo se definen las variables instancia.
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    # la funcion __repr__ se llama cuando se quiere mostrar el objeto en pantalla
    def __repr__(self):
        return self.name

class Money(object):
    "Represent an amount of money"
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    #def base_currency_amount(self):

    #keep watching the video tomorrow   

    def __repr__(self) :
        return '{} {}'.format(self.currency.symbol, self.amount) 
