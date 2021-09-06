import math


def fib(n):
    """
    Imprime os números da sequência de Fibonacci até o número n.
    """
    i, j = 0, 1
    while i < n:
        print(i, end=' ')  # O argumento end pode ser usado para evitar uma nova linha após a saída
        i, j = j, i + j  # Atualiza pelos valores antigos i<--j(antigo) e j<--i(antigo)+j(antigo)
    return


def fib_lista(n):
    """Função que retorna uma lista contendo os números da sequência de Fibonacci até o número n."""
    lista = []
    i, j = 0, 1
    while i < n:
        lista.append(i)
        i, j = j, i + j
    return lista


def fib2(m):
    """
    Imprime os m primeiros números da sequência de Fibonacci.
    Entrada:
        int m: inteiro positivo que representa a quantidade de números a serem calculados

    Saída:
        Não retorna algum valor (None), mas imprime o m primeiros números da sequência
        Fibonacci
    """
    n = 0
    a1 = 0
    a2 = 1
    while n < m:
        print(a1, end=' ')  # O argumento end pode ser usado para evitar uma nova linha após a saída
        aux = a2
        a2 = a2 + a1
        a1 = aux
        n = n + 1
    return


def eh_primo(n):
    """
    Calcula se n é numero primo ou não
    Entrada;
        int n: número Natural maior que 1
    """
    if n == 2:
        return True
    if n % 2 == 0: #Verifica se n é par, maior que 2
        return 2
    for x in range(3, round(math.sqrt(n))+1,2): # x=3,5,7,9,...,round(sqrt(n))
        if n % x == 0:     # verifica se n é divisível por x
            return x

    return True

def lista_numeros_primos(m):
    """
    Calcula os números primos de 2 a m
    Entrada;
        int n: número Natural maior que 1
    """
    for n in range(2, m):
        resultado = eh_primo(n)
        if resultado == True:
            print(n, 'é um número primo')
        else:
            print(n, 'igual', resultado, '*', n // resultado)

    return None