class Calculadora:
    def __init__(self,numero01,numero02):
        self.numero01 = numero01
        self.numero02 = numero02
    def adcao(self):
        if self.numero01:
            soma = self.numero01 + self.numero02
            print(f"o resultado da soma é {soma}")
            return
    def multiplicar(self):
        mult = self.numero01 * self.numero02
        print(f"o resultado da soma é {mult}")
        return
    def divisao(self):
        divi = self.numero01 / self.numero02
        print(f"o resultado da divisao é {divi}")
        return
    def subtracao(self):
        sub = self.numero01 - self.numero02
        print(f"o resultado da subitracao é {sub}")
