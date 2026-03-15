""" Aplicação do Gerador Linear Congruencial
     Algoritmo que produz uma sequência de números pseudo-aleatório calculados com uma função linear em trecho.
        A fórmula é: X_{n+1} = (a * X_n + c) mod m, onde:
        - X é a sequência de números pseudo-aleatórios
        - a é o multiplicador
        - c é o incremento
        - m é o módulo
    Esta aplicação solicita também o número de repetições para gerar a sequência desejada.
"""

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