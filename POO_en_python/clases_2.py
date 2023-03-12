# clases que saben que responder

"""Para que un objeto sepa responder a los operadores suma, resta, multiplicacion y division
 se deben definir los metodos magicos add,sub,mul y truediv respectivamente"""


class Currency(object):
    "Represents a currency"

    # el metodo __init__ se llama cuando se inicializa la clase. 
    # en este metodo se definen las variables instancia.
    def __init__(self, name, symbol, factor):
        self.name = name
        self.symbol = symbol
        self.factor = factor
    
    #convierte la cantidad de una moneda diferente a la moneda elegida como base
    def convert_amount_to_base_currency(slef,aNumber):
        return aNumber * slef.factor
    
    #convierte la cantidad de la moneda base al otro tipo de moneda
    def convert_amount_from_base_currency(self,aNumber):
        return aNumber / self.factor
    
    def __repr__(self):
        return self.name

class Money(object):
    "Represent an amount of money"
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def bas_currency_amount(self):
        return self.currency.convert_amount_to_base_currency(self.amount)
    
    "suma la cantidad ingresada convertida a la moneda base y devuelve la cantidad resultante convertida al tipo de moneda ingresado"
    def __add__(self,anAmountOfMoney):
        amount =self.bas_currency_amount() + anAmountOfMoney.base_currency_amount()
        amount =self.currency.convert_amount_from_base_currency(amount)
        return Money(amount,self.currency)
    
    "Similar a la suma"
    def __sub__(self,anAmountOfMoney):
        amount =self.bas_currency_amount() - anAmountOfMoney.base_currency_amount()
        amount =self.currency.convert_amount_from_base_currency(amount)
        return Money(amount,self.currency)
    
    "multiplica el monto por el numero recibido"
    def __mul__(self, aNumber):
        return Money(self.amount * aNumber, self.currency)
    
    def __trediv__(self, aNumber):
        return Money(self.amount / aNumber, self.currency)
    
    def __repr__(self):
        return '{} {}'.format(self.currency.symbol, self.amount)
    
dolar = Currency('dolar', 'U$S', 1)
pesos = Currency('pesos (Mex)','$',1/20)

one_dolar = Money(1,dolar)
one_peso = Money(1,pesos)