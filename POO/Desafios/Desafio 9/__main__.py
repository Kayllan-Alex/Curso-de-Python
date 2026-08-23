from poligono import Quadrado, Circulo
from rich import print, inspect


def main():
    q = Quadrado(20)
    c = Circulo(2)

    print(f"Um quadrado {q.lado} tem um perímetro de {q.perimetro():.1f}cm²")
    print(f"Um quadrado de {q.lado} tem uma área de {q.area():.1f}cm²")
    print(f"Um circulo {c.raio} tem um perímetro de {c.perimetro():.1f}cm²")
    print(f"Um circulo de {c.raio} tem uma área de {c.area():.1f}cm²")

    inspect(q, methods=True)
    inspect(c, methods=True)


if __name__ == "__main__":
    main()
