import math,cmath


def fib(n):
    """
    Imprime os números da sequência de Fibonacci até o número n.
    """
    i, j = 0, 1
    while i < n:
        print(i, end=' ')  # O argumento end pode ser usado para evitar uma nova linha após a saída
        i, j = j, i + j  # Atualiza pelos valores antigos i<--j(antigo) e j<--i(antigo)+j(antigo)
    return None


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
    return None


def eh_primo(n):
    """
    Calcula se n é numero primo ou não
    Entrada:
        int n: número Natural maior que 1
    Saída:
        Retorma True se n é primo, em caso contrário retorna o menor divisor
        de n, maior ou igual a 2, isto é o menor número primo que pode
        dividir n
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
    Entrada:
        int m: número Natural maior que 2
    Saída;
        None.  Mas imprime todos os numéros primos e não primos de 2 até m.
    """
    for n in range(2, m):
        resultado = eh_primo(n)
        if resultado == True:
            print(n, 'é um número primo')
        else:
            print(n, 'igual', resultado, '*', n // resultado)

    return None

def lista_numeros_primos2(m):
    """
    Calcula os primeiro m números primos
    Entrada:
        int m: número Natural maior que 0
    Saída;
        None. Mas imprime todos os numéros primos e não primos até o m-ésimo número primo.
        (Do número 2 em diante)
    """
    n=0
    k=2
    while n < m: # n=1,2,3,..,m
        resultado = eh_primo(k)
        if resultado == True:
            print(k, 'é um número primo')
            n=n+1
        else:
            print(k, 'igual', resultado, '*', k // resultado)
        k=k+1
    return None

def celsius_to_fahrenheit(c):
    """
    Converte Celsius para Fahrenheit
    Entrada:
        float c: temperatura em Celsius
    Saída;
        float f: temperatura em Fahrenheit.
    """
    return (c*9/5)+32

def nl():
    """Imprime nova linha com asteristicos *********************************************"""
    print('\n***************************************************************************\n')
    return None

def fahrenheit_to_celsius(f):
    """
    Converte Fahrenheit para Celsius
    Entrada:
        float f: temperatura em Fahrenheit
    Saída;
        float c: temperatura em Celsius.
    """
    return (f-32)*5/9

def Baskara(a,b,c):
    delta = b*b-4*a*c
    if delta < 0:
        raiz=math.sqrt(-delta)
        z1=complex(-b/(2*a), raiz/(2*a))
        z2=complex(-b/(2*a), -raiz/(2*a))
        print('A raíses complexas são: ',z1,' e ', z2)
        return [-1,z1,z2]
    else:
        raiz = math.sqrt(delta)
        x1 = (-b + raiz) / (2 * a)
        x2 = (-b - raiz) / (2 * a)
        print('A raíses reais são:', x1, ' e ', x2)
        return [+1,x1, x2]