def geradorLinearCongruencial(a, c, m, x, n):
    sequencia = [x]
    for _ in range(n):
        x = (a * x + c) % m
        sequencia.append(x)
    return sequencia
 
def main():
    multiplicador = int(input("Digite o multiplicador (a): "))
    incremento = int(input("Digite o incremento (c): "))
    modulo = int(input("Digite o módulo (m): "))
    semente = int(input("Digite a semente (x0): "))
    numeroDeRepeticoes = int(input("Quantos números deseja gerar? "))

    resultado = geradorLinearCongruencial(multiplicador, incremento, modulo, semente, numeroDeRepeticoes)
    print("Sequência gerada: ", resultado)

if __name__ == "__main__":
    main()