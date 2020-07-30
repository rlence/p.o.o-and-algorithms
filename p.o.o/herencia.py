class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


    def area(self):
        return self.base * self.altura


class Cuadrado(Rectangulo):

    #cotructor de la clase
    def __init__(self, lado):
        #contructor de la clase padre
        super().__init__(lado, lado)


if __name__ == '__main__':
    rectangulo = Rectangulo(base=3, altura=4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=4)
    print(cuadrado.area())