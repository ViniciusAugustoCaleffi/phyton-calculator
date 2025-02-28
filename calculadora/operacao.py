import math

class Operacao:
    def __init__(self): #construtor
        self.num1 = 0
        self.num2 = 0
    def coletar(self, num1, num2): #criando o metodo coletar
        self.num1 = num1
        self.num2 = num2

    def somar(self,num1, num2):

        self.coletar(num1,num2) #ultilizando o metodo coletar
        return self.num1 + self.num2

    def subtrair(self,num1,num2):

        self.coletar(num1,num2)
        return self.num1 - self.num2

    def multiplicar(self,num1,num2):
        self.coletar(num1,num2)
        return self.num1 * self.num2

    def dividir(self,num1,num2):
        self.coletar(num1,num2)
        if self.num2 <= 0:
            return "Impossivel dividir!"
        else:
            return self.num1 / self.num2

    def tabuada(self,num1):
        resultado = ""
        for i in range(0,11,1):
            resultado += f'\n{num1} * {i} = {num1 * i}  '
        return resultado

    def potencia(self,base,expoente):
        return pow(base,expoente)

    def raiz(self,num):
        return math.sqrt(num)

    def numeros(self, num1):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f'\n{num1} + {i} = {num1 + i}  '
        return resultado

    def pares(self,num1):

        resultado = ""
        for i in range(0, 11, 1):
            resultado += f'\n{num1} + {i} = {num1 + i}  '
        return resultado

