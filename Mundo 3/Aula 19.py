try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Digite apenas números")
except ZeroDivisionError:
    print("Divisão por zero não existe")
except KeyboardInterrupt:
    print("O usuário não informou os dados")
except Exception as erro:
    print(f"O problema encontrado foi {erro.__class__}")
else:
    int(f"O resultado é {r:.1f}")
finally:
    print("Fim do programa")
